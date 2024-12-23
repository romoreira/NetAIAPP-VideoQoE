import http from 'k6/http';

export let options = {
    stages: [
        { duration: '1m', target: 50 }, // 50 usuários em 1 minuto
        { duration: '1m', target: 200 }, // escala até 200 usuários
        { duration: '1m', target: 0 }, // reduz para 0
    ],
};

export default function () {
    http.get('http://127.0.0.1:8080/hls/stream.m3u8');
}
