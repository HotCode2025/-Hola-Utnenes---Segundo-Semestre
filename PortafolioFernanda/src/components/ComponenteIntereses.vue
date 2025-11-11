// ...existing code...
<script setup>
import { ref } from 'vue';

const intereses = ref([
  'Organización y planificación de proyectos',
  'Aprendizaje continuo y nuevas herramientas digitales',
  'Innovación y mejora de procesos',
  'Diseño y confección de ropa',
  'Estilo y creatividad aplicada al diseño'
]);
</script>

<template>
  <div class="intereses-contenedor" role="list">
    <h3 class="titulo-intereses">Intereses</h3>
    <ul class="contenedor-lista">
      <li
        class="item"
        v-for="int in intereses"
        :key="int"
        role="listitem"
      >
        {{ int }}
      </li>
    </ul>
  </div>
</template>

<style scoped>
.intereses-contenedor {
  background: linear-gradient(135deg, #ffe6f0, #f0fff0); /* rosa claro a lima muy suave */
  border: 2px solid #ff69b4; /* rosa fuerte */
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 4px 10px rgba(255, 105, 180, 0.2);
  color: #333;
}

.titulo-intereses {
  color: #ff1493; /* rosa intenso */
  font-size: 1.8rem;
  margin-bottom: 1rem;
  text-align: center;
  text-shadow: 1px 1px 0 #fff;
}

.contenedor-lista {
  list-style: none;
  padding: 0;
  margin: 0;
}

.item {
  background-color: #fafffa; /* blanco con tinte lima */
  border-left: 6px solid #32cd32; /* lima vibrante */
  margin-bottom: 0.75rem;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  transition: transform 0.2s ease, background-color 0.3s ease;
  font-weight: 500;
}

.item:hover {
  background-color: #ffe4ec; /* rosa claro al pasar el mouse */
  transform: scale(1.02);
}
</style>
