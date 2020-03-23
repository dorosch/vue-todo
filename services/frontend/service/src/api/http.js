import axios from 'axios'


const API = axios.create({
  baseURL: 'http://0.0.0.0:8001',
})

export default API
