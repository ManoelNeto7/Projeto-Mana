import { useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const router = useRouter();

  const handleLogin = async () => {
    try {
      const response = await axios.post('/api/users/login', { username, password });
      alert(response.data.message);
      router.push('/dashboard');
    } catch (error) {
      alert(error.response?.data?.error || 'Erro ao fazer login');
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Login</h1>
      <input
        type="text"
        placeholder="Usuário"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        style={{ display: 'block', margin: '10px auto', padding: '10px', width: '200px' }}
      />
      <input
        type="password"
        placeholder="Senha"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        style={{ display: 'block', margin: '10px auto', padding: '10px', width: '200px' }}
      />
      <button onClick={handleLogin} style={{ padding: '10px 20px', marginTop: '20px' }}>
        Entrar
      </button>
    </div>
  );
}
