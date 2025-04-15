import sys
import xbmcplugin
import xbmcgui

def main():
    url = sys.argv[0]
    handle = int(sys.argv[1])

    li = xbmcgui.ListItem(label="Película de ejemplo")
    xbmcplugin.addDirectoryItem(handle, url + "/play?video=1", li, False)

    xbmcplugin.endOfDirectory(handle)

if __name__ == "__main__":
    main()
