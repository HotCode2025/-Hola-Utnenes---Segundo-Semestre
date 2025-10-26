<script setup>
//                          OTAR
const nombreOtar='Otar Kebadze';
const descripcionOtar='Técnico Universitario en Programacion - UTN / FullStack MERN ';
const residenciaOtar = 'Ciudad - Mendoza , Argentina';
const presentacionOtar = 'Amante de la tecnologia, futuro tecnico en programacion. Bienvenidos al portafolio de UTNENES';
const redesSocialesOtar = [
    {id:1, nombre:'Linkedin', src: 'src/assets/linkedin.png',url:'https://www.google.com.ar'},
    {id:2, nombre:'Instagram', src: 'src/assets/instagram.png',url:'https://www.google.com.ar'},
    {id:3, nombre:'Github', src: 'src/assets/github.png',url:'https://www.google.com.ar'},
    {id:4, nombre:'linkedin', src: 'src/assets/resume.png',url:'https://www.google.com.ar'},
];
const telefonoOtar = '📞 Telefono Personal: +5426574154452'
//                          GABRIEL
//                          JOACO
//                          FERNANDO
//                          FERNANDA
//                          FLORENCIA
//                          EMMANUEL
//                          SERENA 
//                          MATIAS
//                          AMELIA

</script>

<template>
    <section class="datos-personales">
        <h1>Portafolio Utnenes Cohorte 2025 - Utn San Rafael</h1>
        <!--                        OTAR                                -->
        <div class="card">
            <h2>{{ nombreOtar }}</h2>
            <h2>{{ descripcionOtar }}</h2>
            <p>{{ presentacionOtar }}</p>
            <ul class="container-lista">
               <li v-for='red in redesSocialesOtar' :key='red.id'>
                <a :href='red.url'><img class='icon-redsocial' width='35rem' :src='red.src' :alt='red.name'></a>
            </li>
            </ul >
            <h3>{{ telefonoOtar }}</h3>
            <h4>{{ residenciaOtar }}</h4>
        </div>
        <!--                        GABRIEL                                -->
        <div class="card">
            <h2>Gabriel</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
                <!--                        JOACO                                -->
        <div class="card">
            <h2>Joaquin</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
        <!--                        FERNANDO                                -->
        <div class="card">
            <h2>Fernando</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
        <!--                        FERNANDA                                -->
        <div class="card">
            <h2>Fernanda</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
        <!--                        FLORENCIA                                -->
        <div class="card">
            <h2>Florencia</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
        <!--                        EMMANUEL                                -->
        <div class="card">
            <h2>Emmanuel</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
        <!--                        SERENA                                -->
        <div class="card">
            <h2>Serena Olmedo</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
        <!--                        MATIAS                                -->
        <div class="card">
            <h2>Matias Tobares</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
        <!--                        AMELIA                                -->
        <div class="card">
            <h2>Amelia Villar</h2>
            <h2>Tecnico Universitario en Programacion</h2>
            <p>Desarrollador Web - ful lstack MERN / Futuro Tecnico en Programacion. Bienveindos al portfolio de UTNENES
            </p>
            <ul class="container-lista">
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Linkedin</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Instagram</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Github</li>
                <li><a href=""><img src="" alt="" class="icon-redsocial"></a>Curricul um Vitae</li>
            </ul >
            <h3>📞 Telefono Personal: +5426574154452</h3>
            <h4>San Rafael - Mendoza , Argentina</h4>
        </div>
    </section>
</template>

<style scoped>
h1{
    font-size: 2.5rem;

}

h3{
    font-size: 1.2rem;
    font-weight: 600;
}

p{
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.card{
    background-color: rgb(13, 63, 104);
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    text-align: center;
}
.card:hover{
   box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

.container-lista{
    display: flex;
    justify-content: center;
    list-style: none;
    padding: 0;
    margin: 0;
    text-align: center;
}

.icon-redsocial{
    align-items: center;
    background-color: aliceblue;
    border-radius: 50%;
    padding: 2px;
    margin: 5px;
    box-shadow: 0 0 5px rgba(95, 124, 205  , 0.934);
}

.icon-redsocial:hover{
    background-color: rgb(84, 97, 107);
    box-shadow: 0 0 5px rgba(251, 249, 249, 0.934);
}

</style>