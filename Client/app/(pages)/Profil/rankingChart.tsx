import React from 'react';
import { Line } from 'react-chartjs-2';
import { GameElo } from '@/model/elo';
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
  const labels = ['-2', '0', '1'];
  const datasets = [];
  const eloScores: { [key: string]: GameElo } = {};


  for (const gameId in eloData) {
    const game = eloData[gameId].videogame;
    const eloScore = eloData[gameId].score;


    if (!eloScores[game.name]) {
      eloScores[game.name] = {
        label: '', 
        data: [0, 0], 
        borderColor: `rgb(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255})`,
        backgroundColor: 'rgba(0, 0, 0, 0.1',
      };
    }

    if (eloData[gameId].date === '20-10-2023') {
      eloScores[game.name].data[0] = eloScore;
    } else if (eloData[gameId].date === '21-10-2023') {
      eloScores[game.name].data[1] = eloScore;
    }
  }


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
        display: false,
      },
    },
  };

  return <Line style={{ marginTop: '50px' }} options={options} data={data} />;
}
