// 在 user.ts 中
import {AxiosResponse} from 'axios';
import http from '@/util/http';

export function getUserInfo(userInfo: UserInfo): Promise<AxiosResponse> {
    return http({
        url: '/api/user/info',
        method: 'get',
        params: userInfo
    });
}

// 显式声明 userInfo 的类型
interface UserInfo {
    // 根据实际情况定义 userInfo 的属性
    username: string;
    password: string;
}
