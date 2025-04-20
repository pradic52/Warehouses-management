import { ipcMain, app } from 'electron'
import fs from 'fs'
import path from 'path'

ipcMain.on('upload-image', (event: Electron.IpcMainEvent, imageData, fileName) => {
  try {
    const uploadDir = path.join(app.getPath('userData'), 'uploads')

    // Créer le dossier s’il n'existe pas
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true })
    }

    const savePath = path.join(uploadDir, fileName)

    // Écriture du fichier en base64
    fs.writeFileSync(savePath, imageData, 'base64')

    // Réponse au renderer
    event.reply('image-saved', savePath)
  } catch (error) {
    if (error instanceof Error) {
      console.error('Erreur lors de l’enregistrement de l’image:', error)
      event.reply('image-saved-error', error.message)
    } else {
      console.error('Erreur inconnue lors de l’enregistrement de l’image:', error)
      event.reply('image-saved-error', 'Erreur inconnue')
    }
  }
})
