<script setup>
//                  IMPORTACIONES

import iconPython from "/src/assets/python-127-svgrepo-com.svg";
import iconJavascript from "/src/assets/javascript-file-svgrepo-com.svg";
import iconJava from "/src/assets/java-svgrepo-com.svg";
import iconHtmlCss from "/src/assets/html-svgrepo-com.svg";
import { ref } from "vue";

// Estructura correcta: `habilidades` es un array de categorías,
// cada categoría tiene una propiedad `habilidad` que es un array
const habilidades = ref([
  {
    id: 1,
    nombre: "Lenguajes De Programacion",
    habilidad: [
      { id: 1, nombre: "Python", nivel: 40, src: iconPython },
      { id: 2, nombre: "Javascript", nivel: 55, src: iconJavascript },
      { id: 3, nombre: "Java", nivel: 35, src: iconJava },
      { id: 4, nombre: "HTML / CSS", nivel: 55, src: iconHtmlCss },
    ],
  }
]);
</script>

<template>
  <div>
    <div class="skills-contenedor">
      <div class="skills-categoria" v-for="hab in habilidades" :key="hab.id">
        <h3>{{ hab.nombre }}</h3>
        <ul class="skills">
          <li class="skill"
              v-for="hab2 in hab.habilidad"
              :key="hab2.id"
              :data-level="hab2.nivel">
            <div class="skill-header">
              <img :src="hab2.src" :alt="hab2.nombre" v-if="hab2.src" />
              <span>{{ hab2.nombre }}</span>
            </div>
            <div class="skill-level">
              <div class="skill-level-bar" :style="{ width: hab2.nivel + '%' }"></div>
            </div>
            <div class="skill-level-text">{{ hab2.nivel }}%</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.skills-contenedor {
  background: linear-gradient(135deg, #fff0f5, #f0fff0); /* rosa claro a lima suave */
  border: 2px solid #ff69b4;
  border-radius: 14px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(255, 105, 180, 0.2);
}

.skills-categoria {
  margin-bottom: 2rem;
}

.skills-categoria h3 {
  color: #ff1493;
  font-size: 1.6rem;
  margin-bottom: 1rem;
  text-align: center;
  text-shadow: 1px 1px 0 #fff;
}

.skills {
  list-style: none;
  padding: 0;
  margin: 0;
}

.skill {
  background-color: #fafffa;
  border-left: 6px solid #32cd32;
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 10px;
  transition: transform 0.2s ease, background-color 0.3s ease;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.skill:hover {
  background-color: #ffe4ec;
  transform: scale(1.02);
}

.skill-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-weight: 600;
  color: #333;
}

.skill-header img {
  width: 32px;
  height: 32px;
  object-fit: contain;
  border-radius: 50%;
  border: 2px solid #ff69b4;
  background-color: #fff;
}

.skill-level {
  background-color: #e0ffe0;
  border-radius: 6px;
  height: 10px;
  overflow: hidden;
  position: relative;
}

.skill-level-bar {
  background-color: #32cd32;
  height: 100%;
  width: 0%;
  transition: width 0.5s ease;
}

.skill[data-level] .skill-level-bar {
  width: calc(attr(data-level percentage));
}

.skill-level-text {
  font-size: 0.9rem;
  color: #ff1493;
  text-align: right;
  font-weight: 500;
}
</style>
