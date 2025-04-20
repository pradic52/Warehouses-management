import { shell, BrowserWindow } from 'electron'
import { join } from 'path'
import { is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'
import { registerRoute } from '../lib/electron-router-dom'
import { RouterId } from '@globaltype/router'

// 🔧 Fonction générique pour créer une fenêtre
//    On contraint `options.id` à WindowId
function createWindow(options: { id: RouterId; htmlFile?: string }): BrowserWindow {
  const window = new BrowserWindow({
    width: 900,
    height: 670,
    show: false,
    autoHideMenuBar: true,
    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  window.on('ready-to-show', () => {
    window.show()
  })

  window.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  // Chargement dev vs prod
  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    window.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    const htmlToLoad = options.htmlFile ?? join(__dirname, '../renderer/index.html')
    window.loadFile(htmlToLoad)
  }

  // 🔌 Enregistrement de la route avec un ID typé
  registerRoute({
    id: options.id,
    browserWindow: window,
    htmlFile: join(__dirname, '../renderer/index.html')
  })

  return window
}

// 🏠 Fenêtre principale
export function createMainWindow(): void {
  createWindow({ id: 'main' })
}

// ⚙️ Fenêtre de configuration
export function createSetupWindow(): void {
  createWindow({ id: 'setup' })
}
