import { createApp } from 'vue'
import App from './App.vue'
import 'aos/dist/aos.css'
import AOS from 'aos'
import '@fortawesome/fontawesome-free/css/all.css'

const app = createApp(App)
app.mount('#app')

AOS.init({
  duration: 1200,
  once: true,
})