<template>
  <div class="charts">
    <div class="donuts">
      <div class="chart">
        <p>Total de formulários preenchidos</p>
        <Chart
          class="donutchart"
          type="doughnut"
          :data="donutData"
          :options="chartOptions"
        />
      </div>
      <div class="chart">
        <p>Satisfação Total</p>
        <Chart
          class="piechart"
          type="pie"
          :data="pieData"
          :options="chartOptions"
        />
      </div>
    </div>
    <div class="chart">
        <p>Importância de cada tópico pelos alunos</p>
      <Chart
        class="barchart"
        type="bar"
        :data="stackedData"
        :options="stackedOptions"
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      stackedData: {
        labels: [
          "Q1",
          "Q2",
          "Q3",
          "Q4",
          "Q5",
          "Q6",
          "Q7",
          "Q8",
          "Q9",
          "Q10",
          "Q11",
          "Q12",
          "Q13",
        ],
        datasets: [
          {
            type: "bar",
            label: "Alta",
            backgroundColor: "#c22a1f",
            data: [50, 25, 12, 48, 90, 76, 42, 25, 50, 27, 33, 88, 19],
          },
          {
            type: "bar",
            label: "Média",
            backgroundColor: "#881c16",
            data: [21, 84, 24, 75, 37, 65, 34, 22, 12, 48, 90, 76, 26],
          },
          {
            type: "bar",
            label: "Baixa",
            backgroundColor: "#ffccc9",
            data: [41, 52, 24, 74, 23, 21, 32, 17, 49, 62, 92, 55, 68],
          },
        ],
      },

      stackedOptions: {
        plugins: {
          tooltips: {
            mode: "index",
            intersect: false,
          },
          legend: {
            labels: {
              color: "#495057",
            },
          },
        },
        scales: {
          x: {
            stacked: true,
            ticks: {
              color: "#495057",
            },
            grid: {
              color: "#ebedef",
            },
          },
          y: {
            stacked: true,
            ticks: {
              color: "#495057",
            },
            grid: {
              color: "#ebedef",
            },
          },
        },
      },

      donutData: {
        labels: ["A", "B", "C"],
        datasets: [
          {
            label: "# of Votes",
            data: [300, 50, 100],
            backgroundColor: ["#c22a1f", "#881c16", "#ffccc9"],
            hoverBackgroundColor: ["#c22a1f", "#881c16", "#ffccc9"],
          },
        ],
      },

      pieData: {
        labels: ["Ótimo", "Bom", "Regular", "Ruim"],
        datasets: [
          {
            data: [300, 50, 100,75],
            backgroundColor: ["#c22a1f", "#881c16", "#ffccc9", "#ff9a94"],
            hoverBackgroundColor: ["#c22a1f", "#881c16", "#ffccc9", "#ff9a94"],
          },
        ],
      },

      chartOptions: {
        legend: {
          labels: {
            fontColor: "#495057",
          },
        },
      },
    };
  },
};
</script>

<style lang="scss" scoped>
.charts {
  width: 100%;
  height: 95%;
  padding: 60px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;

  .chart {
    padding: 20px;
    border-radius: 15px;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
  }

  .donuts {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 25%;
    margin-right: 20px;

    .donutchart {
      margin-bottom: 20px;
    }
  }
}

@media (max-width: 1000px) {
  .charts {
    flex-direction: column;
    width: 100%;

    .donuts {
      flex-direction: row;
      margin: 0 0 20px 0;
      width: 100%;

      .donutchart {
        margin: 0 20px 0 0;
      }
    }
  }
}
</style>
