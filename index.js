import Link from 'next/link';

export default function Home() {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Sistema de Vendas</h1>
      <Link href="/login">
        <a style={{ fontSize: '20px', color: 'blue' }}>Acessar Login</a>
      </Link>
    </div>
  );
}
