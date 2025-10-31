<script setup>
import { ref } from "vue";

// estructura correcta: `habilidades` es un array de categorías,
// cada categoría tiene una propiedad `habilidad` que es un array
const habilidades = ref([
  {
    id: 1,
    nombre: "Lenguajes De Programacion",
    habilidad: [
      { id: 1, nombre: "Python", nivel: "MEDIO", src: "/src/components/icons/python.png" },
      { id: 2, nombre: "Javascript", nivel: "MEDIO", src: "/src/components/icons/js.png" },
      { id: 3, nombre: "Java", nivel: "MEDIO", src: "/src/components/icons/java.png" },
      { id: 4, nombre: "HTML / CSS", nivel: "MEDIO", src: "/src/components/icons/html-css.png" },
    ],
  },
  {
    id: 2,
    nombre: "Frameworks Y Librerias",
    habilidad: [
      { id: 1, nombre: "Vue", nivel: "MEDIO", src: "/src/components/icons/vue.png" },
      { id: 2, nombre: "React", nivel: "MEDIO", src: "/src/components/icons/react.png" },
      { id: 3, nombre: "Bootstrap", nivel: "MEDIO", src: "/src/components/icons/bootstrap.png" }
    ],
  },
  {
    id: 3,
    nombre: "Herramientas Y Software",
    habilidad: [
      { id: 1, nombre: "Git", nivel: "NORMAL", src: "/src/components/icons/git.png" },
      { id: 2, nombre: "Github", nivel: "NORMAL", src: "/src/components/icons/github.png" },
      { id: 3, nombre: "Figma", nivel: "NORMAL", src: "/src/components/icons/figma.png" },
      { id: 4, nombre: "Visual Studio Code", nivel: "AVANZADO", src: "/src/components/icons/visual.png" },
    ],
  },
  {
    id: 4,
    nombre: "Bases De Datos",
    habilidad: [
      { id: 1, nombre: "MySql", nivel: "MEDIO", src: "/src/components/icons/mysql.png" },
      { id: 2, nombre: "MongoDb", nivel: "MEDIO", src: "/src/components/icons/mongo.png" },
      { id: 4, nombre: "PostgreSQL", nivel: "BASICO", src: "/src/components/icons/postgre.png" },
    ],
  },
  {
    id: 5,
    nombre: "Idiomas",
    habilidad: [
      { id: 1, nombre: "Español", nivel: "AVANZADO", src: "/src/components/icons/español.png"},
      { id: 2, nombre: "Ingles", nivel: "MEDIO", src: "/src/components/icons/ingles.png" },
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
          <li class="skill" v-for="hab2 in hab.habilidad" :key="hab2.id">
            <img :src="hab2.src" :alt="hab2.nombre" v-if="hab2.src" />
            <span>{{ hab2.nombre }} - {{ hab2.nivel }}</span>
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
    margin-bottom: 20px;
}

.skills-categoria h3{
    display: flex;
    justify-content: left;
    margin-bottom: 10px;
    font-size: 1.5em;
    color: aliceblue;
    font-size:1.5em;
    font-weight: bold;
}

.skill{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    background-color: rgba(241, 245, 243, 0.856);
    padding: 0.3em;
    border-radius: 8px;
    box-shadow: 0px 4px 12px rgba(2, 151, 151, 0.963);
    flex: 1 1 200;
    max-width: 250px;
}

.skills {
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    gap: 20px;
}

.skill:hover{
    background-color: rgba(2, 151, 151, 0.963);
    font-size: 1.1em;
    transition: 2s ease;
}

.skill img{
    width: 35px;
    height: 35px;
}

.skill span{
    font-size: 1em;
    color: #333;
}

@media(max-width : 768px){
    .skills-categoria h3 , .skill{
        justify-content: center;
    }
}
</style>
