@service
def rain_radar_animation(ms_per_frame = 500, basemap_file = '/config/www/rain_radar/rain_radar_basemap.jpg', input_folder = '/config/www/rain_radar/frames', output_folder = '/config/www/rain_radar'):
    """
    Compile rain radar snapshots into an animated GIF, ordered alphabetically by filename. ms_per_frame is the number of milliseconds to display each frame. basemap_file is the absolute path to the basemap image. input_folder is the absolute path to the folder containing the snapshots. output_folder is the absolute path to where to save the output.
    """
    import os
    from PIL import Image

    frames = [Image.open(input_folder + '/' + frame) for frame in sorted(os.listdir(input_folder))]
    overlaid_frames = []
    for frame in frames:
        basemap = Image.open(basemap_file)
        basemap = basemap.resize(frame.size)
        basemap.paste(frame, (0,0), mask = frame)
#        basemap_text = ImageDraw.Draw(basemap)
#        basemap_text.text((0,0), frame.filename[23:31] + ' at ' + frame.filename[31:35], fill = (255,255,255))
        overlaid_frames.append(basemap)
    overlaid_frames[0].save(output_folder + '/rain_radar_animation_' + frames[-1].filename[42:54] + '.gif', format = 'GIF', append_images = overlaid_frames, save_all = True, duration = 200, loop = 0)
# .  overlaid_frames[0].save(output_folder + '/rain_radar_animation.gif', format = 'GIF', append_images = overlaid_frames, save_all = True, duration = 200, loop = 0)