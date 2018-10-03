<template>
    <div>
        <p>Home page</p>
        <p>Get log from API :</p>
        <ul>
            <li v-for="log in logs">
                {{ log }}
            </li>
        </ul>
        <button @click="getLog">New log</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            logs: ""
        }
    },
    methods: {
        getLog() {
            this.log = this.getLogFromBackend()
        },
        getLogFromBackend() {
            const path = `http://localhost:5000/api/log`
            axios.get(path).then(response => {
                this.logs = response.data.logs
            }).catch(error => {
                console.log(error)
            })
        }
    }
}

</script>
    
