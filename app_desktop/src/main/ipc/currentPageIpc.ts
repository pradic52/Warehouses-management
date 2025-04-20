import { ipcMain, BrowserWindow } from 'electron'

ipcMain.on('get-window-id', (event) => {
  const window = BrowserWindow.getFocusedWindow()
  event.returnValue = window?.id
})
