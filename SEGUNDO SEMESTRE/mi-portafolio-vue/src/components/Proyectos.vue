<script setup>
defineOptions({ name: 'ProyectosSection' })
import { ref } from 'vue'

const proyectos = ref([
  {
    id: 1,
    titulo: 'Asistente de estudios',
    descripcion: 'Aplicación en PSeInt para organizar tareas académicas.'
  },
  {
    id: 2,
    titulo: 'Página de ecommerce',
    descripcion: 'Diseño de tienda online con formulario de pedidos.'
  },
  {
    id: 3,
    titulo: 'Portafolio personal',
    descripcion: 'Este mismo sitio web como carta de presentación.'
  }
])
</script>

<template>
  <section id="proyectos">
    <h2>Proyectos</h2>
    <div class="proyectos-grid">
      <article v-for="p in proyectos" :key="p.id" class="proyecto">
        <h3>{{ p.titulo }}</h3>
        <p>{{ p.descripcion }}</p>
      </article>
    </div>
  </section>
</template>

<style scoped>
.proyectos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.2rem;
  align-items: start;
}
.proyecto {
  min-height: 160px;
  padding: 1.2rem;
  border-radius: 10px;
  background: var(--card-bg, #1f1f1f);
  color: #f2f2f2;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  box-shadow: 0 6px 16px rgba(0,0,0,0.35);
}
.proyecto h3 {
  margin: 0 0 0.6rem 0;
  color: #fff;
  font-size: 1.05rem;
}

.proyectos-grid { padding: 0 0.6rem; }
</style>
