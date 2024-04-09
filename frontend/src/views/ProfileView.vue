<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import { useStore } from 'vuex'
import { PaperAirplaneIcon } from '@heroicons/vue/24/outline';
</script>
<template>
    <section
        class="container w-full md:w-1/3 min-w-10 mx-auto mt-5 bg-gray-50 rounded-md border border-blue-400 p-5 shadow-2xl">
        <div class="row pb-5">
            <h1 class="text-center text-cyan-600 uppercase bg-white p-3 rounded-md shadow-sm"> Perfil Empresa</h1>
        </div>
        <div class="grid grid-cols-1 gap-4 ">
            <div class="flex flex-row  gap-3">
                <label for="name" class="text-sm font-light w-1/2">RUC:</label>
                <input type="text" id="name" class="input w-full border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Nombre:</label>
                <input type="text" id="name" class="input w-full border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Nombre Contacto</label>
                <input type="text" id="name" class="input w-full border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Email:</label>
                <input type="text" id="name" class="input w-full border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Telefono:</label>
                <input type="text" id="name" class="input w-full border border-gray-300 rounded-md" />
            </div>
            <div class="flex justify-end">
                <button class="btn btn-primary btn-sm">
                    <PaperAirplaneIcon class="w-5 h-5 text-white" />
                    Guardar
                </button>
            </div>
        </div>
    </section>
</template>