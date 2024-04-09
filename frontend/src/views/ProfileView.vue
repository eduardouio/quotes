<script setup>
import { RouterLink } from 'vue-router'
import { ref } from 'vue'
import { useStore } from 'vuex'
import { PaperAirplaneIcon } from '@heroicons/vue/24/outline';
</script>
<template>
    <section class="container w-7/12 mx-auto mt-1 bg-gray-100 rounded-sm p-5">
        <div class="row pb-5">
            <h1 class="text-center text-cyan-600 uppercase shadow-sm"> Perfil Empresa</h1>
        </div>
        <div class="grid grid-cols-1 gap-4 lg:grid-cols-2">
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">RUC:</label>
                <input type="text" id="name" class="input w-full input-sm border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Nombre:</label>
                <input type="text" id="name" class="input w-full input-sm border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Nombre Contacto</label>
                <input type="text" id="name" class="input w-full input-sm border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Email:</label>
                <input type="text" id="name" class="input w-full input-sm border border-gray-300 rounded-md" />
            </div>
            <div class="flex flex-row justify-end gap-3">
                <label for="name" class="text-sm font-light w-1/2">Telefono:</label>
                <input type="text" id="name" class="input w-full input-sm border border-gray-300 rounded-md" />
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