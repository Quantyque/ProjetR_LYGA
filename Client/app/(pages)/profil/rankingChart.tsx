import React from 'react';
import { Line } from 'react-chartjs-2';
import { Elo } from '@/model/logic/elo';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export default function RankingChart(props: any) {
  const { eloData } = props;
  const labels = ['Before Last Game', 'Last Game', 'Current'];
  const datasets: any[] = [];
  const eloScores: any[] = [];

  // Trier les données par date
  const sortedEloData = eloData.sort((a: any, b: any) => a.date.localeCompare(b.date));

  sortedEloData.forEach((elo: any) => {
    const game = elo.videogame;
    const eloScore = elo.score;

    if (!eloScores[game.name]) {
      eloScores[game.name] = {
        label: game.name,
        data: [0, 0, 0],
        borderColor: `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`,
        backgroundColor: 'rgba(0, 0, 0, 0.1)',
      };
    }

    // Mettre à jour les données en fonction de la date
    switch (elo.date) {
      case '20-10-2023':
        eloScores[game.name].data[0] = eloScore;
        break;
      case '21-10-2023':
        eloScores[game.name].data[1] = eloScore;
        break;
      // Ajouter d'autres cas pour d'autres dates si nécessaire
      default:
        eloScores[game.name].data[2] = eloScore;
        break;
    }
  });

  for (const gameName in eloScores) {
    datasets.push(eloScores[gameName]);
  }

  const data = {
    labels,
    datasets,
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        display: true,
      },
    },
  };

  return <Line style={{ marginTop: '50px' }} options={options} data={data} />;
}