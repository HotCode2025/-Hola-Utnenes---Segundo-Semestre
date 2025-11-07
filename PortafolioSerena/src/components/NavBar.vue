<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const navegacion = ref([
  { id: 1, nombre: 'Sobre Mí', enlace: '#sobremi' },
  { id: 2, nombre: 'Estudios', enlace: '#estudios' },
  { id: 3, nombre: 'Experiencia', enlace: '#experiencia' },
  { id: 4, nombre: 'Habilidades', enlace: '#habilidades' },
  { id: 5, nombre: 'Proyectos', enlace: '#proyectos' },
  { id: 6, nombre: 'Contacto', enlace: '#contacto' }
])

// theme toggle removed per request

// IntersectionObserver para marcar la sección activa en la navegación
const activeSection = ref('')
let observer = null

function observeSections(){
  const sections = document.querySelectorAll('section[id]')
  if(!sections.length) return

  observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting && entry.intersectionRatio > 0.4){
        activeSection.value = entry.target.id
      }
    })
  }, { threshold: [0.4], rootMargin: '-30% 0px -40% 0px' })

  sections.forEach(s => observer.observe(s))
}

onMounted(() => {
  observeSections()
})

onBeforeUnmount(() => {
  if(observer) observer.disconnect()
})
</script>

<template>
  <header>
    <div class="header-container">
      <h1 class="titulo">
        <span class="prompt-left">&gt;</span>
        Serena Olmedo
        <span class="prompt-right">&lt;</span>
      </h1>
      <p class="subtitulo">Técnico en Programación</p>

      <nav>
        <ul class="navigation">
          <li v-for="nav in navegacion" :key="nav.id">
            <a
              :href="nav.enlace"
              :class="{ active: activeSection === nav.enlace.replace('#','') }"
            >
              {{ nav.nombre }}
            </a>
          </li>
        </ul>
      </nav>

      <!-- theme toggle removed -->
    </div>
  </header>
</template>

<style scoped>
.theme-toggle{ position: absolute; right: 1rem; top: 1.4rem }
.theme-toggle button{ background: transparent; border: 2px solid var(--primary-color); color: var(--primary-color); padding:0.25rem 0.6rem; border-radius:999px; cursor:pointer }
.theme-toggle button:hover{ background:var(--primary-color); color:var(--bg-color) }
</style>
