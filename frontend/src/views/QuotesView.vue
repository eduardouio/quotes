<script setup>
import {
    BeakerIcon, ArrowRightCircleIcon, ArrowDownCircleIcon,
    MapPinIcon, BuildingStorefrontIcon, PlusCircleIcon,
    PencilSquareIcon, TrashIcon, CheckCircleIcon,
    ArrowLeftIcon, HomeIcon, CalendarDaysIcon,
    BellAlertIcon
} from '@heroicons/vue/24/outline';
import { useStore, mapGetters } from 'vuex';
import { computed, onMounted, ref, reactive } from 'vue';

const store = useStore();
let country = ref('');
let supplier = ref(null);
let qoute = reactive({});
let idxModify = ref(false);
let confirmSend = ref(false);
let idxQoute = ref(0);
let closeOrder = ref(false);

const resetQoute = function () {
    qoute = {
        country: '',
        supplier: {},
        portOrigin: '',
        portDestination: '',
        transitDays: 0,
        gOrigin: 0,
        currencyGo: 'USD',
        freight: 0,
        currencyFreight: 'USD',
        localExpenses: 0,
        freeDays: 0,
        offerDays: 0
    }
}

onMounted(() => {
    store.getters.getQoutes;
    resetQoute();
})

const ports = computed(() => {
    return store.getters.getPortsSupplier(supplier.value);
})

const addQoute = function (qoute) {
    qoute.supplier = supplier.value;
    qoute.country = country.value;
    if (idxModify.value) {
        store.commit('changeQoute', { idx: idxQoute.value, qoute });
        idxModify.value = false;
        supplier.value = null;
        return resetQoute();
    }
    store.commit('addQuote', qoute);
    supplier.value = null;
    return resetQoute();
};

const modifyQoute = function (myQoute) {
    idxModify.value = true;
    supplier.value = myQoute.supplier;
    country.value = myQoute.country;
    qoute = myQoute;
};

const setSupplier = function (mySupplier) {
    supplier.value = mySupplier;
    const myQoute = store.getters.getQoute(supplier.value)
    if (myQoute.qoute) {
        idxModify.value = true
        idxQoute.value = myQoute.idx
        return modifyQoute(myQoute.qoute);
    }
    resetQoute();
};

const sendData = function () {
    store.dispatch('sendData', store.state.supplierQoutes);
    confirmSend.value = false;
    resetQoute();
    country.value = '';
    supplier.value = null;
    closeOrder.value = true;
};

</script>
<template>
    <div>
        <div v-if="closeOrder" class="p-40 text-center text-3xl text-green-600 font-light flex flex-col items-center">
            <CheckCircleIcon class="h-20 w-20" />
            <span class="p-10">
                INFORMACION ENVIADA CORRECTAMENTE
            </span>
            <span class="p-10 text-gray-600 font-light">
                GRUPO CVL agradece su participación en el concurso, no pondremos en contacto una vez culminado el
                proceso
            </span>
        </div>
        <div v-else>
            <nav class="navbar bg-slate-800/10 shadow-md h-0">
                <div class="navbar-start">
                    <img src="https://sts-ndt.com/cordovez/statics/img/logo_cvl.png" alt="logo CVL"
                        class="w-20 h-auto border">
                    <a class="">Grupo CVL</a>
                </div>
                <div class="navbar-end">
                    <ul tabIndex={0} className="flex flex-row menu">
                        <li><a>Perfil</a></li>
                        <li><a>Cotizaciones</a></li>
                    </ul>
                </div>
            </nav>
            <section class="container container-lg mx-auto pt-5">
                <div class="grid grid-cols-12 gap-2">
                    <div
                        class="countries menu col-span-2 border border-gray-300 mb-10 border-b-8 border-b-green-500 border-t-8 border-t-green-500 rounded-sm border-l-0 border-r-0">
                        <ul v-for="item in store.getters.getCountries" :key="item" class="text-end">
                            <li class="p-2 border-b  hover:bg-cyan-500 rounded-l-xl hover:border-b-4 hover:border-cyan-700 hover:text-white"
                                :class="{ 'border-b-4 border-red-600': country === item }"
                                @click="country = item; supplier = null">
                                {{ item }}
                            </li>
                        </ul>
                    </div>
                    <div class="col-span-10 border rounded-md border-b p-4">
                        <div v-if="country">
                            <div class="flex justify-center gap-4 w-full bg-zinc-600">
                                <span class="text-xl font-light text-white">
                                    <span v-if="!supplier" class="text-cyan-100">Selecciones Un Proveedor De La
                                        Lista</span>
                                    <span v-else>{{ supplier.nombre }}</span>
                                </span>
                            </div>
                            <div class="grid grid-cols-12 gap-2 w-full mt-4">
                                <div class="col-span-3">
                                    <ul v-for="mySupplier in store.getters.getSupplier(country)"
                                        :key="mySupplier.nombre">
                                        <li class="flex justify-between border-l-8 border-l-sky-500 p-2 border mb-1 border-gray-300 border-r-gray-600 rounded-md border-r-8 rounded-l-full shadow hover:bg-cyan-500 text-sm"
                                            :class="{ 'border-b-4 border-b-yellow-400': supplier === mySupplier }"
                                            @click="setSupplier(mySupplier)">
                                            <CheckCircleIcon class="h-5 w-5 text-green-500"
                                                v-if="store.getters.getSuppliersQouted(mySupplier.nombre)" />
                                            {{ mySupplier.nombre }}
                                        </li>
                                    </ul>
                                    <div class="pt-10">
                                        <button @click="country = ''" class="btn btn-sm btn-info font-light">
                                            <HomeIcon class="h-5 w-5" />
                                            Inicio
                                        </button>
                                    </div>
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
                                        <label :for="qoute.portOrigin" class="col-span-2 text-end text-sm">Puerto
                                            Origen:</label>
                                        <select v-model="qoute.portOrigin"
                                            class="col-span-2 text-end text-sm input-sm border border-gray-300 focus:bg-yellow-200 rounded-md">
                                            <option value="">seleccione...</option>
                                            <option v-for="itm in supplier.puertos" :value="itm" :key="itm">{{ itm }}
                                            </option>
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
                                        <input v-model="qoute.offerDays"
                                            class="input input-sm border border-gray-300 text-right focus:bg-yellow-200 w-full col-span-2"
                                            type="number" step="0">
                                        <div class="col-span-8 p-3 text-end">
                                            <button class="btn btn-info btn-sm font-light mr-5" @click="country = ''">
                                                <HomeIcon class="h-5 w-5" />
                                                Inicio
                                            </button>
                                            <button class="btn btn-info btn-sm font-light" @click="addQoute(qoute)">
                                                <ArrowDownCircleIcon class="h-5 w-5" />
                                                Guardar Cotización
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
                            <table class="table table-xs">
                                <thead>
                                    <tr class="bg-gray-600 text-white font-light text-md text-center">
                                        <td class="border">#</td>
                                        <td class="border">Pais</td>
                                        <td class="border">incoterm</td>
                                        <td class="border">Puerto O</td>
                                        <td class="border">Llegada</td>
                                        <td class="border">D Trans</td>
                                        <td class="border">D Libres</td>
                                        <td class="border">G Origen</td>
                                        <td class="border">Flete</td>
                                        <td class="border">G Locales</td>
                                        <td class="border">Vigencia</td>
                                        <td class="border">Acciones</td>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="myQoute, idx in store.state.supplierQoutes " :key="myQoute"
                                        class="text-sm font-light text-nowrap">
                                        <td class="border text-end">{{ idx + 1 }}</td>
                                        <td class="border">
                                            {{ myQoute.country }}
                                            <br />
                                            <small class="text-xm text-slate-600 font-light">{{ myQoute.supplier.nombre
                                                }}</small>
                                        </td>
                                        <td class="border">{{ myQoute.supplier.incoterm }}</td>
                                        <td class="border">
                                            {{ myQoute.portOrigin }}
                                        </td>
                                        <td class="border">
                                            {{ myQoute.portDestination }}
                                        </td>
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
                                        <td class="border">
                                            <div class="flex justify-between">
                                                <CalendarDaysIcon class="h-4 w-4 text-cyan-600" />
                                                <span>{{ myQoute.offerDays }} días</span>
                                            </div>

                                        </td>
                                        <td class="border text-end">
                                            <div class="flex justify-between">
                                                <span @click="store.commit('deleteQoute', myQoute)">
                                                    <TrashIcon class="h-4 w-4 text-orange-500" />
                                                </span>
                                                <span @click="modifyQoute(myQoute)">
                                                    <PencilSquareIcon class="h-4 w-4 text-cyan-600" />
                                                </span>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                            <div class="bg-red-100 p-10 rounded mt-5 flex justify-between">
                                <p class="flex gap-3 text-cyan-800 align-middle">
                                    <BellAlertIcon class="h-5 w-5 text-red-500" />
                                    UNA VEZ QUE HAYA TERMINADO DE AGREGAR LAS COTIZACIONES
                                    <br />
                                    DE CLIC EN EL BOTÓN PARA ENVIAR LA INFORMACIÓN
                                </p>

                                <button v-if="!confirmSend" class="btn btn-md btn-info text-white font-light"
                                    @click="confirmSend = true">
                                    <ArrowRightCircleIcon class="h-5 w-5" />Enviar Cotizaciones
                                </button>
                                <button v-if="confirmSend" class="btn btn-md btn-success text-white font-light"
                                    @click="sendData">
                                    <ArrowRightCircleIcon class="h-5 w-5" />Confirmar
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <footer class="footer footer-center p-10 bg-gray-700 rounded text-white">
                <aside>
                    <p>Todos Los Derechos Reservados</p>
                    <small>desarrollado por Eduardo Villota
                        <a class="text-cyan-300" href="mailto:eduardouio7@gmail.com">eduardouio7@gmail.com</a>
                    </small>
                </aside>
            </footer>
        </div>
    </div>
</template>
<style scoped>
@media print {
    .navbar {
        display: none;
    }

    .countries {
        display: none;
    }
}
</style>