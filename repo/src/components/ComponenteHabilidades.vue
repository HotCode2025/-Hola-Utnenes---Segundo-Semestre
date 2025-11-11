<!-- Habilidades.vue -->
<script setup>
    import { ref } from "vue";

    /*
      🔧 IMPORTES DE ÍCONOS
      
      import iconPython from "../assets/python-127-svgrepo-com.svg";
      import iconJavascript from "../assets/javascript-file-svgrepo-com.svg";
      import iconJava from "../assets/java-svgrepo-com.svg";
      import iconHtmlCss from "../assets/html-svgrepo-com.svg";

      Si preferís alias "@", agrega en vite.config.js:
      import { fileURLToPath, URL } from 'node:url'
      export default defineConfig({
        resolve: { alias: { '@': fileURLToPath(new URL('./src', import.meta.url)) } }
      })
      y luego importá así:
    */
    import iconPython from "@/assets/python-127-svgrepo-com.svg";
    import iconJavascript from "@/assets/javascript-file-svgrepo-com.svg";
    import iconJava from "@/assets/java-svgrepo-com.svg";
    import iconHtmlCss from "@/assets/html-svgrepo-com.svg";

    const habilidades = ref([
        {
            id: 1,
            nombre: "Lenguajes de Programación",
            habilidad: [
                { id: 1, nombre: "Python", nivel: 45, src: iconPython },
                { id: 2, nombre: "JavaScript", nivel: 60, src: iconJavascript },
                { id: 3, nombre: "Java", nivel: 35, src: iconJava },
                { id: 4, nombre: "HTML / CSS", nivel: 60, src: iconHtmlCss },
            ],
        },
        {
            id: 2,
            nombre: "Otras Tecnologías",
            habilidad: [
                { id: 1, nombre: "Vue 3 + Vite", nivel: 55, src: null },
                { id: 2, nombre: "WordPress / Elementor", nivel: 70, src: null },
                { id: 3, nombre: "C# (WinForms)", nivel: 50, src: null },
                { id: 4, nombre: "SQL / Access / PostgreSQL", nivel: 45, src: null },
                { id: 5, nombre: "Git / GitHub", nivel: 50, src: null },
            ],
        },
    ]);
</script>

<template>
    <section class="skills-contenedor">
        <div class="skills-categoria" v-for="cat in habilidades" :key="cat.id">
            <h3>{{ cat.nombre }}</h3>
            <ul class="skills" role="list">
                <li class="skill"
                    v-for="hab in cat.habilidad"
                    :key="hab.id"
                    role="listitem"
                    :aria-label="`${hab.nombre} ${hab.nivel}%`">
                    <div class="skill-header">
                        <img v-if="hab.src" :src="hab.src" :alt="hab.nombre" />
                        <span>{{ hab.nombre }}</span>
                    </div>

                    <div class="skill-level" aria-hidden="true">
                        <div class="skill-level-bar" :style="{ width: hab.nivel + '%' }"></div>
                    </div>

                    <div class="skill-level-text">{{ hab.nivel }}%</div>
                </li>
            </ul>
        </div>
    </section>
</template>

<style scoped>
    .skills-contenedor {
        padding: 2rem;
    }

    .skills-categoria {
        margin-bottom: 2rem;
    }

        .skills-categoria h3 {
            display: flex;
            justify-content: left;
            margin-bottom: 1rem;
            font-size: 1.5em;
            color: var(--color-heading);
            font-weight: bold;
        }

    .skills {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 1rem;
    }

    .skill {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        background-color: var(--color-background-soft);
        padding: 1rem;
        border-radius: var(--border-radius);
        border: 1px solid var(--color-border);
        transition: all var(--transition-fast);
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
        width: 0%; /* se anima hasta el valor inline */
    }

    .skill-level-text {
        font-size: 0.8em;
        color: var(--color-text);
        opacity: 0.8;
        text-align: right;
    }

    .skill:hover {
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

    .skill img {
        width: 35px;
        height: 35px;
        transition: transform var(--transition-fast);
    }

    .skill:hover img {
        transform: scale(1.1);
    }

    .skill span {
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
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
        transition: left 0.5s;
    }

    .skill:hover::before {
        left: 100%;
    }

    @media(max-width : 768px) {
        .skills-categoria h3 {
            justify-content: center;
            text-align: center;
        }

        .skills-contenedor {
            padding: 1rem;
        }
    }

    @media(max-width : 480px) {
        .skills {
            grid-template-columns: 1fr;
        }
    }
</style>
