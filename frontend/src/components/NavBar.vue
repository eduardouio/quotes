<script setup>
import { RouterLink } from 'vue-router'
import { computed, ref } from 'vue'
import { useStore } from 'vuex'
import { CurrencyDollarIcon, UserIcon, DeviceTabletIcon } from '@heroicons/vue/24/outline';


const store = useStore()
const activeClass = ref('shadow-sm rounded-lg border border-gray-300 text-green-600')
const current = computed(() => store.getters.getSelectedMenu)

</script>
<template>
    <nav class="navbar bg-slate-800/10 shadow-md h-0">
        <div class="navbar-start">
            <img src="https://sts-ndt.com/cordovez/statics/img/logo_cvl.png" alt="logo CVL" class="w-20 h-auto border">
            <a class="">Grupo CVL</a>
        </div>
        <div class="navbar-end">
            <ul tabIndex={0} class="flex flex-row menu items-center">
                <li @click="store.commit('changeMenuSelected', 'home')" :class="{ [activeClass]: current === 'home' }">
                    <RouterLink to="/">
                        <CurrencyDollarIcon class="w-6 h-6" /> Cotizaciones
                    </RouterLink>
                </li>
                <li @click="store.commit('changeMenuSelected', 'profile')"
                    :class="{ [activeClass]: current === 'profile' }">
                    <RouterLink to="/profile">
                        <UserIcon class="w-6 h-6" />
                        Perfil
                    </RouterLink>
                </li>
            </ul>
        </div>
    </nav>
</template>