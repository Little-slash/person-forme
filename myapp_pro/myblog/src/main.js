import { createApp } from 'vue'
import App from './App.vue'
import "./assets/reset.css";
import "./assets/font/font.css"
import axios from 'axios'
const app = createApp(App);

app.config.globalProperties.$url = 'http://127.0.0.1:8000/';
app.config.globalProperties.$http = axios;
app.mount('#app')
