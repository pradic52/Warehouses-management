import { ipcMain, IpcMainEvent } from 'electron'
import fs from 'fs'
import { DataSetupType } from '@globaltype/object/dataType'
import { configPath } from '@main/config'

ipcMain.handle('is-first-run', () => {
  return !fs.existsSync(configPath)
})

ipcMain.on('setup-complete', (event: IpcMainEvent, data: DataSetupType): void => {
  console.log(event)
  fs.writeFileSync(configPath, JSON.stringify(data, null, 2))
})
