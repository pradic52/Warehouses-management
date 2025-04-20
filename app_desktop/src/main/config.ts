import { app } from 'electron'
import fs from 'fs'
import path from 'path'

const configPath: string = path.join(app.getPath('userData'), 'config.json')

function isFirstRun(): boolean {
  return !fs.existsSync(configPath)
}

export { isFirstRun, configPath }
