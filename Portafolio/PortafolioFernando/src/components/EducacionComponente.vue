<script setup>
import { ref } from 'vue'
const arreglo = ref([
  { id: 1, fecha: '2025 - Actualidad', titulo: 'Técnico Universitario en Programación', descripcion: 'Actualmente me encuentro estudiando la Tecnicatura Universitaria en Programacion, adquiriendo conocimientos sólidos en desarrollo de software y metodologías ágiles.', enlace: '#' },
  { id: 2, fecha: '2022', titulo: 'iOS & Swift – The complete iOS App Development Bootcamp - Udemy', descripcion: 'He completado el bootcamp integral de desarrollo de aplicaciones para iOS, especializándome en el lenguaje Swift y el framework UIKit. Este curso me ha proporcionado experiencia práctica en el ciclo completo de desarrollo de apps, desde el diseño de la interfaz de usuario y la gestión del layout (Auto Layout) hasta la integración de APIs, bases de datos (Core Data/Realm) y la implementación de patrones de diseño (MVC). Adquirí la habilidad de desplegar aplicaciones funcionales y escalables, enfocándome en la optimización del rendimiento y la adherencia a las guías de diseño de Apple.', enlace: '#' },
  { id: 3, fecha: '2021', titulo: 'FrontEnd - Coderhouse', descripcion: 'He completado el curso intensivo en desarrollo Frontend, adquiriendo dominio en la construcción de interfaces de usuario (UI) modernas y dinámicas. Mi formación abarcó HTML para la estructuración semántica del contenido, CSS para el diseño responsivo y el manejo avanzado de layouts (Grid y Flexbox), y JavaScript para la lógica del lado del cliente. Finalmente, obtuve experiencia práctica con la librería React, desarrollando componentes reutilizables y gestionando el estado de aplicaciones web de una sola página (SPA). Este curso me preparó para transformar diseños en productos digitales funcionales y atractivos.', enlace: '#' },
  { id: 4, fecha: '2010 - 2015', titulo: 'Licenciado en Educación Fisica y Deportes', descripcion: 'Formación integral centrada en la biomecánica, la fisiología del ejercicio y la pedagogía aplicada. Mis estudios me han capacitado para diseñar programas de acondicionamiento físico personalizado y para la prevención de lesiones, utilizando estrategias didácticas efectivas para motivar a grupos de todas las edades. He adquirido competencias en la gestión de eventos deportivos y en la adaptación de actividades para la inclusión, aplicando el conocimiento científico para optimizar tanto el bienestar individual como el rendimiento deportivo.', enlace: '#' }
  
])
</script>

<template>
  <div class="educacion">
    <div class="card" v-for="item in arreglo" :key="item.id">
      <h3>{{ item.titulo }}</h3>
      <span class="fecha">{{ item.fecha }}</span>
      <p>{{ item.descripcion }}</p>
      <a :href="item.enlace" target="_blank">Ver más</a>
    </div>
  </div>
</template>

<style scoped>
.educacion {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}
.card {
  background-color: var(--color-bg-card);
  border-left: 5px solid var(--color-accent);
  padding: 1.5rem;
  border-radius: 10px;
  width: 280px;
  box-shadow: 0 0 15px rgba(255, 213, 79, 0.1);
  transition: 0.3s;
}
.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 0 25px rgba(255, 213, 79, 0.25);
}
.fecha {
  color: var(--color-accent);
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}
a { color: var(--color-accent); font-weight: bold; }
a:hover { text-decoration: underline; }
</style>
