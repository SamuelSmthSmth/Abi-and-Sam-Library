const { app, BrowserWindow } = require('electron')

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    })

    win.setMenuBarVisibility(false)  // 👈 Hides the menu bar

    win.loadFile('src/index.html')
}

app.whenReady().then(() => {
    createWindow()
})
