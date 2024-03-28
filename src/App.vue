<script setup>
import { BeakerIcon, ArrowRightCircleIcon, MapPinIcon, BuildingStorefrontIcon } from '@heroicons/vue/24/outline';
import { RouterLink, RouterView } from 'vue-router'
import { useStore, mapGetters } from 'vuex';
import HelloWorld from './components/HelloWorld.vue'
import { computed, onMounted, ref } from 'vue';

const store = useStore();

onMounted(() => {
  store.state.quotes;
})


</script>
<template>
  <div>
    <nav class="navbar bg-slate-800/10 shadow-md h-0">
      <div class="navbar-start">
        <div class="dropdown md:hidden">
          <div tabindex="0" role="button" class="btn btn-ghost btn-circle">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" />
            </svg>
          </div>
          <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
            <li><a>Homepage</a></li>
            <li><a>Portfolio</a></li>
            <li><a>About</a></li>
          </ul>
        </div>
        <img src="https://sts-ndt.com/cordovez/statics/img/logo_cvl.png" alt="logo CVL" class="w-20 h-auto border">
        <a class="">Grupo CVL</a>
      </div>
      <div class="navbar-end">
        <ul tabIndex={0} className="flex flex-row menu">
          <li><a>Perfil</a></li>
          <li><a>Cotizaciones</a></li>
          <li><a>
              Resumen
            </a></li>
        </ul>
      </div>
    </nav>
    <section class="pb-10">
      <div class="text-sm breadcrumbs w-full">
        <ul>
          <li><a>Inicio</a></li>
          <li><a>Reporte</a></li>
          <li class="text-sky-800">Listado de Cotizaciones</li>
        </ul>
      </div>
    </section>
    <section class="container container-lg mx-auto">
      <div class="grid grid-cols-12 gap-2">
        <span
          class="col-span-2 border-t border-l border-r rounded-sm text-center bg-zinc-200 text-xl p-2 text-teal-600">PAISES</span>
        <span
          class="col-span-10 border-t border-l border-r rounded-sm text-center bg-zinc-200 text-xl p-2 text-teal-600">COTIZACION</span>
        <div class="menu col-span-2 border-l border-r border-b  border-gray-300">
          <ul v-for="item in store.getters.getCountries" :key="item">
            <li
              class="p-2 text-end border-b  hover:bg-cyan-500 rounded-l-xl hover:border-b-4 hover:border-cyan-700 hover:text-white">
              {{ item }}
            </li>
          </ul>
        </div>
        <div class="col-span-10 border-l border-r border-b p-3 border-gray-30">
          <div class="flex justify-center gap-4 w-full bg-zinc-600  rounded-md mb-10 border-b p-4">
            <span class="text-xl font-light text-white">
              GONZALEZ BYAS
            </span>
          </div>
          <div class="grid grid-cols-12 gap-2 w-full">
            <div class="col-span-3">
              <ul v-for="supplier in store.getters.getSupplier('ESPAÑA')" :key="supplier">
                <li
                  class="border-l-8 border-l-sky-500 p-2 border mb-1 border-gray-300 border-r-gray-300 rounded-md border-r-8 rounded-l-full shadow hover:bg-cyan-500">
                  {{
            supplier }}</li>
              </ul>
            </div>
            <div class="col-span-8 bg-slate-100 p-4">
              <div class="flex justify-between">
                <strong>ALEMANIA </strong>
                <div>
                  <strong> Direccion:</strong> Calle 123 y las retamas, mexico guadalajara rwe234563
                </div>
              </div>
              <div class="flex justify-between">
                <div class="">
                  <strong>Inconterm:</strong> FOB
                </div>
                <div class="">
                  <strong>Puertos:</strong> Valencia, Barcelona, Bilbao
                </div>
              </div>
              <hr class="m-3">
              <div class="grid grid-cols-6 gap-2">
                <label for="" class="col-span-1 text-end">Puerto Origen:</label>
                <input class="input input-bordered w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Puerto Destino:</label>
                <input class="input input-bordered *:w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Días Transito:</label>
                <input class="input input-bordered w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Días Libres:</label>
                <input class="input input-bordered *:w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Moneda:</label>
                <input class="input input-bordered w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end ">Gasto Origen:</label>
                <input class="input input-bordered w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Moneda:</label>
                <input class="input input-bordered *:w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Flete:</label>
                <input class="input input-bordered *:w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Gastos Locales:</label>
                <input class="input input-bordered *:w-full col-span-2" type="text">
                <label for="" class="col-span-1 text-end">Días Vigencia:</label>
                <input class="input input-bordered *:w-full col-span-2" type="text">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <RouterView />
  </div>
</template>
