def network_visualisation():
    """
    Compile network visualisation of Home Assistant.
    """
    
    import paramiko
    import os
    import re
    import json
    import yaml
    import networkx as nx
    import matplotlib.pyplot as plt
    
    def input_constructor(loader: yaml.SafeLoader, node: yaml.nodes.ScalarNode) -> str:
        '''Helper to handle !input tags in blueprints'''
        return loader.construct_scalar(node)
      
    def get_loader():
        """Add constructors to PyYAML loader."""
        loader = yaml.Loader
        loader.add_constructor("!input", input_constructor)
        loader.add_constructor("!secret", input_constructor)
        return loader
      
    def traverse(obj, output_list):
        '''Helper function to find all entity_ids in any arbitrary YAML structure'''
        if type(obj) == str:
            for entity_id in re.findall(entity_id_pattern, obj):
                output_list.append(entity_id) 
        elif type(obj) in [list, tuple, set]:
            for i in obj:
                traverse(i, output_list)
        elif type(obj) == dict:
            for key in obj.keys():
                traverse(obj[key], output_list)
    
    def add_edges_without_nonexistent_nodes(g, input_dict):
        '''Checks that in and out nodes are not the same and exist in g, then adds the edge to g'''
        for key in input_dict.keys():
            for i in input_dict[key]:
                if key != i:
                    if key in g.nodes and i in g.nodes:
                        g.add_edge(key, i)
    
    # regex matching for entity ids
    entity_id_pattern = r'[a-z_]+\.[a-zA-z0-9_]+'
    
    with open('/config/.storage/core.device_registry') as f:
        device_registry = json.load(f)
    with open('/config/.storage/core.entity_registry') as f:
        entity_registry = json.load(f)
        
    devices = [(device['id'], device) for device in device_registry['data']['devices']]
    entities = [(entity['entity_id'], entity) for entity in entity_registry['data']['entities'] if (entity['hidden_by'] is None and entity['disabled_by'] is None)]
    areas = [(area, {'type': 'area', 'colour': 'green'}) for area in {device[1]['area_id'] for device in devices if device[1]['area_id'] is not None}]
    
    domains = {entity[1]['entity_id'].split('.')[0] for entity in entities}
    automation_entity_ids = {entity[1]['unique_id']: entity[1]['entity_id'] for entity in entities if entity[1]['entity_id'].split('.')[0] == 'automation'}
    
    device_entity_edges = [(entity[1]['entity_id'], entity[1]['device_id']) for entity in entities if entity[1]['device_id'] is not None]
    area_device_edges = [(device[0],device[1]['area_id']) for device in devices if device[1]['area_id'] is not None]
    area_entity_edges = [(entity[0], entity[1]['area_id']) for entity in entities if entity[1]['area_id'] is not None]
    
    G = nx.Graph()

    G.add_nodes_from(devices)
    G.add_nodes_from(entities)
    G.add_nodes_from(areas)
    
    G.add_edges_from(device_entity_edges)
    G.add_edges_from(area_device_edges)
    G.add_edges_from(area_entity_edges)
    
    for node in G.nodes:
        if 'type' in G.nodes[node].keys():
            if G.nodes[node]['type'] == 'area':
                continue
        elif 'entity_id' in G.nodes[node].keys():
            if G.nodes[node]['entity_id'].split('.')[0] == 'automation':
                G.nodes[node]['type'] = 'automation'
                G.nodes[node]['colour'] = 'red'
            elif G.nodes[node]['entity_id'].split('.')[0] == 'script':
                G.nodes[node]['type'] = 'script'
                G.nodes[node]['colour'] = 'orange'
            else:
                G.nodes[node]['type'] = 'entity'
                G.nodes[node]['colour'] = 'grey'
        else:
            G.nodes[node]['type'] = 'device'
            G.nodes[node]['colour'] = 'black'
            
    with open('/config/automations.yaml') as f:
        automation_list = yaml.load(f, Loader = yaml.Loader)
    with open('/config/scripts.yaml') as f:
        script_dict = yaml.load(f, Loader = yaml.Loader)
        
    blueprints = {automation['use_blueprint']['path'] for automation in automation_list if 'use_blueprint' in automation.keys()}

    G.add_nodes_from([(blueprint, {'type': 'blueprint', 'colour': 'blue'}) for blueprint in blueprints])
    G.add_edges_from([(automation_entity_ids[automation['id']], automation['use_blueprint']['path']) for automation in automation_list if 'use_blueprint' in automation.keys()])
    
    automation_entities = dict()
    for automation in automation_list:
        automation_entities_list = []
        traverse(automation, automation_entities_list)
        automation_entities[automation_entity_ids[automation['id']]] = automation_entities_list
        
    add_edges_without_nonexistent_nodes(G, automation_entities)
    
    script_entities = dict()
    for script in script_dict.keys():
        script_entities_list = []
        traverse(script_dict[script], script_entities_list)
        script_entities['script.' + script] = script_entities_list
    
    add_edges_without_nonexistent_nodes(G, script_entities)
    
    with open('/config/aircons.yaml') as f:
        aircon_list = yaml.load(f, Loader = yaml.Loader)
    aircon_entity_edges = []
    for aircon in aircon_list:
        aircon_entity_edges.extend([(aircon['unique_id'],aircon['heater']), (aircon['unique_id'],aircon['target_sensor'])])
    G.add_edges_from(aircon_entity_edges)
    
    with open('/config/covers.yaml') as f:
        cover_list = yaml.load(f, Loader = yaml.Loader)
    cover_entities = dict()
    for cover in cover_list[0]['covers']:
        cover_entities_list = []
        traverse(cover_list[0]['covers'][cover], cover_entities_list)
        cover_entities['cover.' + cover] = cover_entities_list
    add_edges_without_nonexistent_nodes(G, cover_entities)
    
    with open('/config/fans.yaml') as f:
        fan_dict = yaml.load(f, Loader = yaml.Loader)[0]['fans']
    fan_entities = dict()
    for fan in fan_dict.keys():
        fan_entities_list = []
        traverse(fan_dict[fan], fan_entities_list)
        fan_entities['fan.' + fan] = fan_entities_list
    add_edges_without_nonexistent_nodes(G, fan_entities)
    
    with open('/config/sensors.yaml') as f:
        sensor_list = yaml.load(f, Loader = get_loader())
    for sensor in sensor_list:
        if sensor['platform'] == 'statistics':
            if sensor['unique_id'] in G.nodes and sensor['entity_id'] in G.nodes:
                G.add_edge(sensor['unique_id'], sensor['entity_id'])
    
    with open('/config/switches.yaml') as f:
        switch_dict = yaml.load(f, Loader = yaml.Loader)[0]['switches']
    switch_entities = dict()
    for switch in switch_dict.keys():
        switch_entities_list = []
        traverse(switch_dict[switch], switch_entities_list)
        switch_entities['switch.' + switch] = switch_entities_list
    add_edges_without_nonexistent_nodes(G, switch_entities)
    
    with open('/config/sensors-template.yaml') as f:
        template_sensor_list = yaml.load(f, Loader = yaml.Loader)
    template_sensor_entities = dict()
    for i in range(len(template_sensor_list)):
        for key in template_sensor_list[i]:
            if 'sensor' in key:
                for j in template_sensor_list[i][key]:
                    template_sensor_entities_list = []
                    traverse(j, template_sensor_entities_list)
                    template_sensor_entities[j['unique_id']] = template_sensor_entities_list
    add_edges_without_nonexistent_nodes(G, template_sensor_entities)
    
    with open('/config/sensors-rest.yaml') as f:
        rest_sensor_list = yaml.load(f, Loader = get_loader())
    rest_sensor_entities = dict()
    for i in range(len(rest_sensor_list)):
        for key in rest_sensor_list[i]:
            if 'sensor' in key:
                for j in rest_sensor_list[i][key]:
                    rest_sensor_entities_list = []
                    traverse(j, rest_sensor_entities_list)
                    rest_sensor_entities[j['unique_id']] = rest_sensor_entities_list
    add_edges_without_nonexistent_nodes(G, rest_sensor_entities)
    
    blueprint_entities = dict()
    for blueprint_path in [path[0] + '\\' + filename for path in os.walk('\\config\\blueprints') for filename in path[2]]:
        with open(blueprint_path, encoding = 'utf-8') as f:
            blueprint_dict = yaml.load(f, Loader = get_loader())
        
        for key in blueprint_dict.keys():
            if key != 'description':
                blueprint_entities_list = []
                traverse(blueprint_dict[key], blueprint_entities_list)
                blueprint_entities['/'.join(blueprint_path.split('\\')[-2:])] = blueprint_entities_list
    
    add_edges_without_nonexistent_nodes(G, blueprint_entities)
    
    spring_pos = nx.spring_layout(G, k = 0.05)
    nodetypes = {G.nodes[node]['type'] for node in G.nodes}
    nodesets = {nodetype: [node for node in G.nodes if G.nodes[node]['type'] == nodetype] for nodetype in nodetypes}
    node_colours = {G.nodes[node]['type']: G.nodes[node]['colour'] for node in G.nodes}
    
    fig01 = plt.figure(figsize = (10,10))
    for nodeset in nodesets.keys():
        nx.draw_networkx_nodes(G, pos = spring_pos, 
                               nodelist = nodesets[nodeset], 
                               node_size = 10,
                               node_color = node_colours[nodeset], label = nodeset)
    nx.draw_networkx_edges(G, pos = spring_pos, width = 0.4, edge_color = 'lightgrey')
    plt.legend()
    plt.axis('off')
    plt.savefig('/config/www/readme_graphics/network_visualisation.png')
    
    G_areas_devices_entities = G.subgraph([node for node in G.nodes if G.nodes[node]['type'] in ['device','area','entity']])
    nx.draw(G_areas_devices_entities, 
            pos = nx.spring_layout(G_areas_devices_entities, k = 0.05), 
            edge_color = 'lightgrey', node_size = 10, 
            node_color = [G_areas_devices_entities.nodes[node]['colour'] for node in G_areas_devices_entities.nodes])
    plt.savefig('/config/www/readme_graphics/graph_areas_devices_entities.png')
    
    largest_connected_component = G_areas_devices_entities.subgraph(max(nx.connected_components(G_areas_devices_entities), key = len))
    spring_pos = nx.spring_layout(largest_connected_component, k = 0.1)
    fig02 = plt.figure(figsize = (10,10))
    plt.subplot(111)
    nx.draw(largest_connected_component, pos = spring_pos, edge_color = 'lightgrey', node_size = 10, node_color = [largest_connected_component.nodes[node]['colour'] for node in largest_connected_component.nodes])
    nx.draw_networkx_labels(largest_connected_component, spring_pos, 
                            {area: area if largest_connected_component.nodes[area]['type'] == 'area' else '' for area in largest_connected_component.nodes})
    plt.savefig('/config/www/readme_graphics/graph_areas_devices_entities_lcc.png')
    
    G_blueprints_automations_scripts = G.subgraph([node for node in G.nodes if G.nodes[node]['type'] in ['automation','script','blueprint']])
    nx.draw(G_blueprints_automations_scripts, 
            pos = nx.spring_layout(G_blueprints_automations_scripts, k = 0.17), 
            edge_color = 'lightgrey', node_size = 20,
            node_color = [G_blueprints_automations_scripts.nodes[node]['colour'] for node in G_blueprints_automations_scripts.nodes])
    plt.savefig('/config/www/readme_graphics/graph_blueprints_automations_scripts.png')