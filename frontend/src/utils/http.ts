import axios from "axios";
import {baseUrl} from "@/utils/config";

// 创建一个 axios 实例
const instance = axios.create({
    baseURL: baseUrl,
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
    },
});


export default instance;