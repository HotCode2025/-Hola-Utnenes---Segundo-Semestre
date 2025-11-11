<script setup>
    const title = "Cristian Gabriel Moya (Gaby)";
    const descripcion = "Técnico en Turismo y Hotelería · Est. Tec. Univ. en Programación (UTN) y Tec. en Análisis de Sistemas (IES21)";
    const residencia = "Malargüe, Mendoza, Argentina";
    const presentacion = "¡Hola! Bienvenido/a a mi portafolio de proyectos. Soy guía y desarrollador en formación. Coordino experiencias de Astroturismo en Malargüe (Payunia Travel) y proyectos STEAM/tecnología, combinando turismo, astronomía y software.";
    const redesSociales = [
        { id: 1, name: 'linkedin', src: 'src/assets/linkedin-svgrepo-com (4).svg', url: '' }, // ← tu LinkedIn (si tenés)
        { id: 2, name: 'instagram', src: 'src/assets/instagram-svgrepo-com.svg', url: 'https://www.instagram.com/ungabymas/' },
        { id: 3, name: 'github', src: 'src/assets/github-svgrepo-com.svg', url: '' }, // ← tu GitHub (si querés sumar)
        { id: 4, name: 'curriculum', src: 'src/assets/square-cv-svgrepo-com (1).svg', url: '' }, // ← link a CV (Drive/Website)
    ];
    const telefono = '+54 260 434 9945';
</script>

<template>
    <section class="datos-personales">
        <div class="card">
            <h1>{{ title }}</h1>
            <h2>{{ descripcion }}</h2>
            <p>{{ presentacion }}</p>

            <ul class="container-lista">
                <li v-for="red in redesSociales" :key="red.id">
                    <a :href="red.url || '#'" target="_blank" rel="noopener">
                        <img :src="red.src"
                             class="icon-redsocial"
                             width="35rem"
                             :alt="red.name" />
                    </a>
                </li>
            </ul>

            <h3>Mi teléfono personal: {{ telefono }}</h3>
            <h4>{{ residencia }}</h4>
        </div>
    </section>
</template>

<style scoped>
    h1 {
        font-size: 2.5rem;
    }

    h5 {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    p {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }

    .card {
        background-color: rgb(28, 43, 52);
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
        text-align: center;
        color: #f3f6f9;
    }

    .container-lista {
        display: flex;
        justify-content: center;
        list-style: none;
        padding: 0;
        margin: 0;
        text-align: center;
    }

    .icon-redsocial {
        align-items: center;
        background-color: aliceblue;
        border-radius: 50%;
        padding: 2px;
        margin: 5px;
        box-shadow: 0 0 5px rgba(35, 134, 209, 0.934);
    }

        .icon-redsocial:hover {
            background-color: rgb(103, 157, 190);
            box-shadow: 0 0 5px rgba(255, 249, 249, 0.934);
        }

    h3 {
        font-size: 1.2rem;
        font-weight: 600;
    }
</style>
