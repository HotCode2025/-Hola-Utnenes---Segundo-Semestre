<script setup>
//                  IMPORTACIONES

import iconPython from "/src/components/icons/python.png";
import iconJavascript from "/src/components/icons/js.png";
import iconJava from "/src/components/icons/java.png";
import iconHtmlCss from "/src/components/icons/html-css.png";

import iconVue from "/src/components/icons/vue.png";
import iconReact from "/src/components/icons/react.png";
import iconBootstrap from "/src/components/icons/bootstrap.png";

import iconGit from "/src/components/icons/git.png";
import iconGithub from "/src/components/icons/github.png";
import iconFigma from "/src/components/icons/figma.png";
import iconVisual from "/src/components/icons/visual.png";

import iconMysql from "/src/components/icons/mysql.png";
import iconMongo from "/src/components/icons/mongo.png";
import iconPostgre from "/src/components/icons/postgre.png";
import iconEspañol from "/src/components/icons/español.png";
import iconIngles from "/src/components/icons/ingles.png";
import { ref } from "vue";

// Estructura correcta: `habilidades` es un array de categorías,
// cada categoría tiene una propiedad `habilidad` que es un array
const habilidades = ref([
  {
    id: 1,
    nombre: "Lenguajes De Programacion",
    habilidad: [
      { id: 1, nombre: "Python", nivel: 70, src: iconPython },
      { id: 2, nombre: "Javascript", nivel: 75, src: iconJavascript },
      { id: 3, nombre: "Java", nivel: 65, src: iconJava },
      { id: 4, nombre: "HTML / CSS", nivel: 85, src: iconHtmlCss },
    ],
  },
  {
    id: 2,
    nombre: "Frameworks Y Librerias",
    habilidad: [
      { id: 1, nombre: "Vue", nivel: 80, src: iconVue },
      { id: 2, nombre: "React", nivel: 70, src: iconReact },
      { id: 3, nombre: "Bootstrap", nivel: 75, src: iconBootstrap },
    ],
  },
  {
    id: 3,
    nombre: "Herramientas Y Software",
    habilidad: [
      { id: 1, nombre: "Git", nivel: 60, src: iconGit },
      { id: 2, nombre: "Github", nivel: 65, src: iconGithub },
      { id: 3, nombre: "Figma", nivel: 55, src: iconFigma },
      { id: 4, nombre: "Visual Studio Code", nivel: 90, src: iconVisual },
    ],
  },
  {
    id: 4,
    nombre: "Bases De Datos",
    habilidad: [
      { id: 1, nombre: "MySql", nivel: 70, src: iconMysql },
      { id: 2, nombre: "MongoDb", nivel: 65, src: iconMongo },
      { id: 4, nombre: "PostgreSQL", nivel: 50, src: iconPostgre },
    ],
  },
  {
    id: 5,
    nombre: "Idiomas",
    habilidad: [
      { id: 1, nombre: "Español", nivel: 100, src: iconEspañol },
      { id: 2, nombre: "Ingles", nivel: 70, src: iconIngles },
    ],
  },
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
              <div class="skill-level-bar"></div>
            </div>
            <div class="skill-level-text">{{ hab2.nivel }}%</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.skills-contenedor{
    padding: 2rem;
}

.skills-categoria{
    margin-bottom: 2rem;
}

.skills-categoria h3{
    display: flex;
    justify-content: left;
    margin-bottom: 1rem;
    font-size: 1.5em;
    color: var(--color-heading);
    font-weight: bold;
}

.skill{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    background-color: var(--color-background-soft);
    padding: 1rem;
    border-radius: var(--border-radius);
    border: 1px solid var(--color-border);
    transition: all var(--transition-fast);
    cursor: pointer;
    position: relative;
    overflow: hidden;
}

.skill-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.skill-level {
    width: 100%;
    height: 6px;
    background-color: var(--color-border);
    border-radius: 3px;
    overflow: hidden;
    position: relative;
}

.skill-level-bar {
    height: 100%;
    background-color: var(--color-primary);
    border-radius: 3px;
    transition: width 1s ease-in-out;
    width: 0%; /* Se controlará con data-level */
}

.skill-level-text {
    font-size: 0.8em;
    color: var(--color-text);
    opacity: 0.8;
    text-align: right;
}

.skills {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
}

.skill:hover{
    background-color: var(--color-background-mute);
    border-color: var(--color-primary);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(163, 230, 53, 0.2);
}

.skill:active {
    transform: translateY(0px);
}

.skill:hover .skill-level-bar {
    background-color: var(--color-hover);
}

.skill img{
    width: 35px;
    height: 35px;
    transition: transform var(--transition-fast);
}

.skill:hover img{
    transform: scale(1.1);
}

.skill span{
    font-size: 1em;
    color: var(--color-text);
    font-weight: 500;
}

.skill::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
    transition: left 0.5s;
}

.skill:hover::before {
    left: 100%;
}


.skill[data-level="100"] .skill-level-bar { width: 100%; }
.skill[data-level="95"] .skill-level-bar { width: 95%; }
.skill[data-level="90"] .skill-level-bar { width: 90%; }
.skill[data-level="85"] .skill-level-bar { width: 85%; }
.skill[data-level="80"] .skill-level-bar { width: 80%; }
.skill[data-level="75"] .skill-level-bar { width: 75%; }
.skill[data-level="70"] .skill-level-bar { width: 70%; }
.skill[data-level="65"] .skill-level-bar { width: 65%; }
.skill[data-level="60"] .skill-level-bar { width: 60%; }
.skill[data-level="55"] .skill-level-bar { width: 55%; }
.skill[data-level="50"] .skill-level-bar { width: 50%; }
.skill[data-level="45"] .skill-level-bar { width: 45%; }
.skill[data-level="40"] .skill-level-bar { width: 40%; }
.skill[data-level="35"] .skill-level-bar { width: 35%; }
.skill[data-level="30"] .skill-level-bar { width: 30%; }
.skill[data-level="25"] .skill-level-bar { width: 25%; }
.skill[data-level="20"] .skill-level-bar { width: 20%; }
.skill[data-level="15"] .skill-level-bar { width: 15%; }
.skill[data-level="10"] .skill-level-bar { width: 10%; }
.skill[data-level="5"] .skill-level-bar { width: 5%; }
.skill[data-level="0"] .skill-level-bar { width: 0%; }

@media(max-width : 768px){
    .skills-categoria h3{
        justify-content: center;
        text-align: center;
    }
    
    .skills-contenedor{
        padding: 1rem;
    }
}

@media(max-width : 480px){
    .skills {
        grid-template-columns: 1fr;
    }
}
</style>
