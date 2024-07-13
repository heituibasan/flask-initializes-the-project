/**
 * 检查传入的值是否为有效的邮箱格式
 * @param email - 要检查的字符串
 * @returns 如果是有效的邮箱格式，返回 true；否则返回 false
 */
export function isValidEmail(email: string): boolean {
    // 正则表达式用于匹配邮箱格式
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}


/**
 * 检查设备为Android或PC
 */
export function checkDevice(): 'android' | 'pc' {
    const userAgent = navigator.userAgent.toLowerCase();
    if (/android/i.test(userAgent)) {
        return 'Android';
    } else {
        return 'PC';
    }
}