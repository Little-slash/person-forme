const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  assetsDir: 'static',
  transpileDependencies: true,
  lintOnSave: false, // 关闭eslint检查
})