const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,

  devServer: {
    proxy: {
      '/': {
        target: 'http://localhost:5000',  // URL of Flask-backend
        changeOrigin: true,
      },
    },
  },
})
