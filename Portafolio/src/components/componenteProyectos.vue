<script setup>
//              IMPORTACIONES
import imagenSrc from '/src/assets/proyecto.jpg';

import {ref} from 'vue';

const proyectos = ref([
    {id:'1' , titulo:'Primer Semestre' , descripcion :'Portafolio Primer semestre Utnenes',linkPagina:'https://otarkebadze.github.io/utnenes-portfolio', linkGithub:'https://github.com/OtarKebadze/utnenes-portfolio', img:'/src/assets/proyecto.jpg'},
    {id:'2' , titulo:'Segundo Semestre' , descripcion :'Portafolio Segundo Semestre Utnenes',linkPagina:'#blank', linkGithub:'#blank', img:imagenSrc},
])
</script>

<template>
  <div class="galeria" >
    <div class="proyecto" v-for='proyecto in proyectos' :key="proyecto.id">
      <img :src=" proyecto.img " alt="Proyecto 1" />
      <div class="proyecto-info">
        <h3>{{ proyecto.titulo }}</h3>
        <p>{{proyecto.descripcion}}</p>
        <div class="proyecto-links">
          <a
            :href="proyecto.linkPagina"
            class="btn-ver-mas"
            target="_blank"
            rel="noopener noreferrer">
            Ver Proyecto
        </a>
          <a
            :href="proyecto.linkGithub "
            class="github-link"
            target="_blank"
            rel="noopener noreferrer"
            >
            Ver codigo en Github
        </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.galeria {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px;
  justify-content: center;
  background: linear-gradient(-45deg, #021526, #373337, #33184b, #162270);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

.proyecto {
  display: flex;
  flex-direction: column;
  border: 2px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  border-color: #f9f9f9;
  max-width: 222px;
  flex: 1 1 300px;
}

.proyecto img {
  width: 100%;
  height: auto;
  display: block;
}

.proyecto-info {
  padding: 15px;
  text-align: center;
}

.proyecto-info h3 {
  margin: 10px 0;
  font-size: 1.3em;
  color: #666;
}

.proyecto-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}

.proyecto-links .btn-ver-mas {
  background-color: #007bff;
  border: 2px solid #007bff;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  transition: all 0.3s ease;
  font-weight: bold;
  display: inline-block;
  width: 100%;
}

.proyecto-links .btn-ver-mas:hover {
  background-color: #0056b3;
  border-color: #0056b3;
  transform: translateY(-2px);
}

.proyecto-links .github-link {
  color: #fff;
  text-decoration: none;
  padding: 5px 10px;
  transition: all 0.3s ease;
  display: inline-block;
  width: 100%;
}

.proyecto-links .github-link:hover {
  text-decoration: underline;
  color: #007bff;
}
</style>
