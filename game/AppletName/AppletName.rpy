## Applet Name
# A short description of a delicious app!
# Author(s): Your Name (@githubusername)
# Copyright: (C) 2018

init python:
    class AppletName(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Applet"
        long_name = "Full Applet Name"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "AppletName"
        author = "Your Name"
        version = "0.0.0"
        description = """\
A wonderful but short description of a delicious applet.
        """

        # Define your icons here. They should be located in 
        # your Applet's Resources/icons/ folder
        icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }

        # Define what permissions your applet will need.
        # See the Applet Manifest wiki page for all possible
        # permissions
        permissions = {pm_notify}
    
    appletname = AppletName()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.

# Sample window
init screen windowname:
    use UIWindow(renpyApp)
    use UIWindowContent
    vbox:
        xanchor -16
        yanchor -68
        xoffset 32
        yoffset 32
        xsize 1216
        ysize 603
        vbox:
            # It is recommended to put your content here
            text "Content":
                style "app_default_text"