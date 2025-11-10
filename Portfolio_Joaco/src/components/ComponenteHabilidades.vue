<script setup>
import { ref } from "vue";

import iconPython from "/src/components/icons/python.png";
import iconJavascript from "/src/components/icons/js.png";
import iconJava from "/src/components/icons/java.png";
import iconHtmlCss from "/src/components/icons/html-css.png";

import iconGit from "/src/components/icons/git.png";
import iconGithub from "/src/components/icons/github.png";
import iconFigma from "/src/components/icons/figma.png";
import iconVisual from "/src/components/icons/visual.png";

import iconEspañol from "/src/components/icons/español.png";
import iconIngles from "/src/components/icons/ingles.png";

const habilidades = ref([
  {
    id: 1,
    nombre: "Lenguajes de Programación",
    habilidad: [
      { id: 1, nombre: "Python", nivel: 70, src: iconPython },
      { id: 2, nombre: "Javascript", nivel: 75, src: iconJavascript },
      { id: 3, nombre: "Java", nivel: 65, src: iconJava },
      { id: 4, nombre: "HTML / CSS", nivel: 85, src: iconHtmlCss },
    ],
  },
  {
    id: 2,
    nombre: "Herramientas y Software",
    habilidad: [
      { id: 1, nombre: "Git", nivel: 60, src: iconGit },
      { id: 2, nombre: "Github", nivel: 65, src: iconGithub },
      { id: 3, nombre: "Figma", nivel: 55, src: iconFigma },
      { id: 4, nombre: "Visual Studio Code", nivel: 90, src: iconVisual },
    ],
  },
  {
    id: 3,
    nombre: "Idiomas",
    habilidad: [
      { id: 1, nombre: "Español", nivel: 100, src: iconEspañol },
      { id: 2, nombre: "Inglés", nivel: 70, src: iconIngles },
    ],
  },
]);
</script>

<template>
  <div class="skills-contenedor">
    <div class="skills-categoria" v-for="hab in habilidades" :key="hab.id">
      <h3>{{ hab.nombre }}</h3>
      <div class="skills-vertical">
        <div
          class="skill-vertical"
          v-for="hab2 in hab.habilidad"
          :key="hab2.id"
          :data-level="hab2.nivel"
        >
          <div class="skill-bar">
            <div class="skill-fill"></div>
          </div>
          <img :src="hab2.src" :alt="hab2.nombre" v-if="hab2.src" />
          <span>{{ hab2.nombre }}</span>
          <p>{{ hab2.nivel }}%</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.skills-contenedor {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  background: linear-gradient(180deg, #0f172a, #1e1b4b);
  border-radius: 16px;
}

/* ----- TITULOS DE CATEGORIA ----- */
.skills-categoria {
  background: rgba(255, 255, 255, 0.05);
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.25);
  backdrop-filter: blur(10px);
}

.skills-categoria h3 {
  font-size: 1.6em;
  color: #c084fc;
  font-weight: 700;
  margin-bottom: 1.5rem;
  border-left: 4px solid #c084fc;
  padding-left: 10px;
  text-transform: uppercase;
}

/* ----- BARRAS VERTICALES ----- */
.skills-vertical {
  display: flex;
  justify-content: center;
  gap: 2rem;
  align-items: flex-end;
  flex-wrap: wrap;
}

.skill-vertical {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  color: #e0e7ff;
  font-weight: 500;
  position: relative;
}

/* Contenedor de la barra */
.skill-bar {
  width: 35px;
  height: 140px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 6px;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: flex-end;
}

/* Barra de relleno morado-azulada */
.skill-fill {
  width: 100%;
  background: linear-gradient(180deg, #a78bfa, #60a5fa);
  border-radius: 6px;
  transition: height 1s ease-in-out;
  height: 0%;
}

/* Control por nivel */
.skill-vertical[data-level="100"] .skill-fill { height: 100%; }
.skill-vertical[data-level="95"] .skill-fill { height: 95%; }
.skill-vertical[data-level="90"] .skill-fill { height: 90%; }
.skill-vertical[data-level="85"] .skill-fill { height: 85%; }
.skill-vertical[data-level="80"] .skill-fill { height: 80%; }
.skill-vertical[data-level="75"] .skill-fill { height: 75%; }
.skill-vertical[data-level="70"] .skill-fill { height: 70%; }
.skill-vertical[data-level="65"] .skill-fill { height: 65%; }
.skill-vertical[data-level="60"] .skill-fill { height: 60%; }
.skill-vertical[data-level="55"] .skill-fill { height: 55%; }
.skill-vertical[data-level="50"] .skill-fill { height: 50%; }

/* Icono y nombre */
.skill-vertical img {
  width: 40px;
  height: 40px;
  margin-top: 0.5rem;
  transition: transform 0.3s ease;
  background: rgba(255, 255, 255, 0.07);
  border-radius: 8px;
  padding: 4px;
}

.skill-vertical:hover img {
  transform: scale(1.1);
}

.skill-vertical span {
  font-size: 1em;
  margin-top: 0.3rem;
}

.skill-vertical p {
  font-size: 0.9em;
  color: #a5b4fc;
}

/* Hover visual */
.skill-vertical:hover .skill-fill {
  filter: brightness(1.3);
  transition: height 0.8s ease-in-out, filter 0.3s ease;
}

@media (max-width: 768px) {
  .skills-vertical {
    gap: 1rem;
  }
}

@media (max-width: 480px) {
  .skills-vertical {
    gap: 0.75rem;
  }
  .skill-bar {
    width: 28px;
    height: 110px;
  }
}
</style>










