@service
def compile_rain_radar_animation(ms_per_frame = 500, basemap_file = '/config/www/rain_radar/rain_radar_basemap.jpg', input_folder = '/config/www/rain_radar/frames', output_folder = '/config/www/rain_radar'):
    '''
    Wrapper for module to compile rain radar snapshots into an animated GIF, ordered alphabetically by filename. ms_per_frame is the number of milliseconds to display each frame. basemap_file is the absolute path to the basemap image. input_folder is the absolute path to the folder containing the snapshots. output_folder is the absolute path to where to save the output.
    '''

    import sys

    if "/config/pyscript/modules" not in sys.path:
        sys.path.append("/config/pyscript/modules")

    from rain_radar_animation import rain_radar_animation
    rain_radar_animation(ms_per_frame, basemap_file, input_folder, output_folder)