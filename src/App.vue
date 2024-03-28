<script setup>
import { BeakerIcon, ArrowRightCircleIcon, MapPinIcon, BuildingStorefrontIcon, PlusCircleIcon, ArrowLeftIcon } from '@heroicons/vue/24/outline';
import { RouterLink, RouterView } from 'vue-router'
import { useStore, mapGetters } from 'vuex';
import HelloWorld from './components/HelloWorld.vue'
import { computed, onMounted, ref, reactive } from 'vue';

const store = useStore();
let country = ref('');
let supplier = ref(null);
let qoute = reactive({});

const resetQoute = function () {
  qoute = {
    country: '',
    supplier: '',
    portOrigin: '',
    portDestination: '',
    transitDays: 0,
    gOrigin: 0,
    currencyGo: 'USD',
    freight: 0,
    currencyFreight: 'USD',
    localExpenses: 0,
    freeDays: 0
  }
}

const ports = computed(() => {
  return store.getters.getPortsSupplier(supplier.value);
})

onMounted(() => {
  store.state.quotes;
  resetQoute();
})

const addQoute = function (qoute) {
  qoute.supplier = supplier.value.nombre;
  qoute.country = country.value;
  store.commit('addQuote', qoute);
  supplier.value = null;
  resetQoute();
};


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
    <section class="container container-lg mx-auto pt-5">
      <div class="grid grid-cols-12 gap-2">
        <div
          class="menu col-span-2 border border-gray-300 mb-10 border-b-8 border-b-green-500 border-t-8 border-t-green-500 rounded-sm border-l-0 border-r-0">
          <ul v-for="item in store.getters.getCountries" :key="item" class="text-end">
            <li
              class="p-2 border-b  hover:bg-cyan-500 rounded-l-xl hover:border-b-4 hover:border-cyan-700 hover:text-white"
              :class="{ 'border-b-4 border-red-600': country === item }" @click="country = item; supplier = null">
              {{ item }}
            </li>
          </ul>
        </div>
        <div class="col-span-10 border rounded-md border-b p-4">
          <div v-if="country">
            <div class="flex justify-center gap-4 w-full bg-zinc-600">
              <span class="text-xl font-light text-white">
                <span v-if="!supplier" class="text-cyan-100">Selecciones Un Proveedor De La Lista</span>
                <span v-else>{{ supplier.nombre }}</span>
              </span>
            </div>
            <div class="grid grid-cols-12 gap-2 w-full mt-4">
              <div class="col-span-3">
                <ul v-for="mySupplier in store.getters.getSupplier(country)" :key="mySupplier.nombre">
                  <li
                    class="border-l-8 border-l-sky-500 p-2 border mb-1 border-gray-300 border-r-gray-600 rounded-md border-r-8 rounded-l-full shadow hover:bg-cyan-500 text-sm"
                    :class="{ 'border-b-4 border-b-yellow-400': supplier === mySupplier }"
                    @click="supplier = mySupplier">
                    {{ mySupplier.nombre }}
                  </li>
                </ul>
              </div>
              <div class="col-span-8 bg-slate-100 p-4" v-if="supplier">
                <div class="grid grid-cols-8">
                  <div class="col-span-2 flex flex-col gap-1">
                    <span class="text-red-800 kbd kbd-sm">{{ country }}</span>
                    <span class="text-red-800 kbd kbd-sm">{{ supplier.incoterm }}</span>
                  </div>
                  <div class="col-span-6 flex flex-col gap-1">
                    <span class="kbd kbd-sm">{{ supplier.direccion }}</span>
                    <span class="kbd kbd-sm">
                      {{ ports }}
                    </span>
                  </div>
                </div>

                <hr class="m-3">
                <div class="grid grid-cols-8 gap-2">
                  <label for="" class="col-span-2 text-end text-sm">Puerto Origen:</label>
                  <select v-model="qoute.portOrigin"
                    class="col-span-2 text-end text-sm input-sm border border-gray-300 focus:bg-yellow-200 rounded-md">
                    <option value="">seleccione...</option>
                    <option v-for="itm in supplier.puertos" :value="itm" :key="itm">{{ itm }}</option>
                  </select>
                  <label for="" class="col-span-2 text-end text-sm">Puerto Destino:</label>
                  <select v-model="qoute.portDestination"
                    class="col-span-2 text-end text-sm input-sm border border-gray-300 focus:bg-yellow-200 rounded-md">
                    <option value="">seleccione...</option>
                    <option value="GUAYAQUIL">GUAYAQUIL</option>
                    <option value="POSORJA">POSORJA</option>
                  </select>
                  <label for="" class="col-span-2 text-end text-sm">Días Tránsito:</label>
                  <input v-model="qoute.transitDays"
                    class="input input-sm border border-gray-300 text-right focus:bg-yellow-200 w-full col-span-2"
                    type="number">
                  <label for="" class="col-span-2 text-end text-sm">Días Libres:</label>
                  <input v-model="qoute.freeDays"
                    class="input input-sm border border-gray-300 text-right focus:bg-yellow-200 w-full col-span-2"
                    type="number">
                  <label for="" class="col-span-2 text-end text-sm ">Gasto Origen:</label>
                  <input v-model="qoute.gOrigin"
                    class="input input-sm border border-gray-300 text-right focus:bg-yellow-200 w-full col-span-2"
                    type="number" step="2">
                  <label for="" class="col-span-2 text-end text-sm">Moneda GO:</label>
                  <select v-model="qoute.currencyGo"
                    class="col-span-2 text-end text-sm input-sm border border-gray-300 focus:bg-yellow-200 rounded-md">
                    <option value="USD">USD</option>
                    <option value="EURO">EURO</option>
                  </select>
                  <label for="" class="col-span-2 text-end text-sm">Flete:</label>
                  <input v-model="qoute.freight"
                    class="input input-sm border border-gray-300 text-right focus:bg-yellow-200 w-full col-span-2"
                    type="number" step="2">
                  <label for="" class="col-span-2 text-end text-sm">Moneda Flete:</label>
                  <select v-model="qoute.currencyFreight"
                    class="col-span-2 text-end text-sm input-sm border border-gray-300 focus:bg-yellow-200 rounded-md">
                    <option value="USD">USD</option>
                    <option value="EURO">EURO</option>
                  </select>
                  <label for="" class="col-span-2 text-end text-sm">Gastos Locales:</label>
                  <input v-model="qoute.localExpenses"
                    class="input input-sm border border-gray-300 text-right focus:bg-yellow-200 w-full col-span-2"
                    type="number" step="2">
                  <label for="" class="col-span-2 text-end text-sm">Días Vigencia Oferta:</label>
                  <input v-model="qoute.freeDays"
                    class="input input-sm border border-gray-300 text-right focus:bg-yellow-200 w-full col-span-2"
                    type="number" step="0">
                  <div class="col-span-8 p-3 text-end">
                    <button class="btn btn-info btn-sm font-light mr-5" @click="country = ''">
                      <ArrowLeftIcon class="h-5 w-5" />
                      Volver
                    </button>
                    <button class="btn btn-info btn-sm font-light" @click="addQoute(qoute)">
                      <PlusCircleIcon class="h-5 w-5" />
                      Agregar Cotización
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div v-if="!country">
            <div class=" text-center text-sm text-gray-800 font-light h-10">
              Para agregar items selecciones un pais de la lista a la izquierda
            </div>
            <table class="table">
              <thead>
                <tr class="bg-gray-600 text-white font-light text-md text-center font-semibold">
                  <td class="border">#</td>
                  <td class="border">Pais</td>
                  <td class="border">Puerto O</td>
                  <td class="border">Llegada</td>
                  <td class="border">D Trans</td>
                  <td class="border">D Libres</td>
                  <td class="border">G Origen</td>
                  <td class="border">Flete</td>
                  <td class="border">G Locales</td>
                  <td class="border">Acciones</td>
                </tr>
              </thead>
              <tbody>
                <tr v-for="myQoute, idx in  store.state.supplierQoutes " :key="myQoute">
                  <td class="border text-end">{{ idx + 1 }}</td>
                  <td class="border">{{ myQoute.country }}</td>
                  <td class="border">{{ myQoute.portOrigin }}</td>
                  <td class="border">{{ myQoute.portDestination }}</td>
                  <td class="border text-end">{{ myQoute.transitDays }}</td>
                  <td class="border text-end">{{ myQoute.freeDays }}</td>
                  <td class="border text-end">
                    <div class="flex justify-between">
                      <span class="badge badge-sm bg-green-300"
                        :class="{ 'bg-red-300': myQoute.currencyGo === 'EURO' }">
                        {{ myQoute.currencyGo }}
                      </span>
                      <span>
                        {{ myQoute.gOrigin.toFixed(2) }}
                      </span>
                    </div>
                  </td>
                  <td class="border text-end">
                    <div class="flex justify-between">
                      <span class="badge badge-sm bg-green-300"
                        :class="{ 'bg-red-300': myQoute.currencyFreight === 'EURO' }">
                        {{ myQoute.currencyFreight }}
                      </span>
                      <span>
                        {{ myQoute.freight.toFixed(2) }}
                      </span>
                    </div>
                  </td>
                  <td class="border text-end">
                    <div class="flex justify-between">
                      <span class="badge badge-sm bg-green-300">USD</span>
                      <span>{{ myQoute.localExpenses.toFixed(2) }}</span>

                    </div>
                  </td>
                  <td class="border text-end">
                    <div class="flex justify-between">
                      <span class="text-red-600">Eliminar</span>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
    <RouterView />
    <footer class="footer footer-center p-10 bg-gray-700 rounded text-white">
      <aside>
        <p>Todos Los Derechos Reservados</p>
        <small>desarrollado por Eduardo Villota
          <a class="text-cyan-300" href="mailto:eduardouio7@gmail.com">eduardouio7@gmail.com</a>
        </small>
      </aside>
    </footer>
  </div>
</template>
