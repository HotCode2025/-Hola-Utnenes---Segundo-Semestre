<script setup>
import { ref } from 'vue'; 


const fechaColor = ref([
  {color: '#41516C'},
  {color: '#FBCA3E'},
  {color: '#E24A68'},
  {color: '#185F8C'},
  {color: '#4CADAD'},
]); 

const educacion = ref([
  {
    fecha: '2025',
    title: 'Tecnicatura Universitaria en Programación',
    descripcion: 'Técnico Universitario en Programación con sólidos conocimientos en el ciclo de desarrollo de software.',
  },
  {
    fecha: '2024',
    title: 'Operador de PC (CCT) - Nivel I y II',
    descripcion: 'Formación completa en Ofimática Profesional. Dominio de Microsoft Office (Word, Excel, PowerPoint y Outlook).',
  },
  {
    fecha: '2022',
    title: 'Moldería y Confección / Lencería, Corsetería y Trajes de Baño',
    descripcion: 'Especialización en patronaje y confección de indumentaria íntima y de playa (lencería, corsetería, moldería).',
  },
]);
</script>

<template>
  <div>
    <ul>
      <li
        v-for="(item, index) in educacion"
        :key="index"
        :style="{ '--fecha-color': fechaColor[index].color }"
      >
        <div class="fecha">{{ item.fecha }}</div>
        <h3 class="title">{{ item.titulo }}</h3>
        <div class="descripcion">{{ item.descripcion }}</div>
      
      </li>
      </ul>
  </div>
</template>

<style scoped>
ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  background-color: #fafffa; /* blanco con tinte lima */
  border-left: 6px solid var(--fecha-color, #32cd32); /* color dinámico por fecha */
  margin-bottom: 1rem;
  padding: 1rem 1.5rem;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(255, 105, 180, 0.15);
  transition: transform 0.2s ease, background-color 0.3s ease;
}

li:hover {
  background-color: #ffe4ec; /* rosa claro al pasar el mouse */
  transform: scale(1.02);
}

.fecha {
  color: var(--fecha-color, #32cd32);
  font-weight: 600;
  font-size: 1rem;
  margin-bottom: 0.5rem;
}

.title {
  color: #ff1493;
  font-size: 1.4rem;
  margin-bottom: 0.5rem;
  text-shadow: 1px 1px 0 #fff;
}

.descripcion {
  color: #444;
  font-size: 1rem;
  line-height: 1.5;
}
</style>
