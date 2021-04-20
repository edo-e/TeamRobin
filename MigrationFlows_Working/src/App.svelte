<script>
	import Papa from "papaparse";
	import Dotting from "./components/Dotting.svelte";
	import { max, sort } from "d3-array";
	import { scaleLinear, scaleLog } from "d3-scale";

	let raw_data = [];
	let z = 0;
	let i = 60;
	let j = 0;
	let start_i = 1;
	let y = 0;
	let last_female = 0;
	let last_male = 0;
	let temp = "";
	let spacing = 16;
	let calculated_length = 0;

	let datapoints_from_app = [];

	$: {
		datapoints_from_app = [];
		raw_data = [];
		Papa.parse("Total_origin_destination.csv", {
			header: true,
			download: true,
			complete: function (results) {
				raw_data = results.data.slice(1, 3000);
			},
		});
	}
	const array_generator = function (array_length, start) {
		calculated_length = Math.floor(array_length / 300000);
		return Array(calculated_length)
			.fill()
			.map((_, idx) => start + 14 + idx * spacing);
	};

	//$: console.log(array_generator(1000 / 200, 5000));

	//,Continent,Region,Destination,Origin,Female_1990,Female_1995,Female_2000,Female_2005,Female_2010,Female_2015,Female_2019,Male_1990,Male_1995,Male_2000,Male_2005,Male_2010,Male_2015,Male_2019
	$: {
		raw_data.forEach((d) => {
			datapoints_from_app = [
				...datapoints_from_app,
				{
					Destination: d.Destination,
					X: 0,
					Y: 0,
					Origin: d.Origin,
					Region: d.Region,
					Continent: d.Continent,
					max: max([+d.Female_1990, 30000]),
					Female_1990: +d.Female_1990,
					Male_1990: +d.Male_1990,
					max: max([
						+d.Male_2019,
						+d.Male_2015,
						+d.Male_2010,
						+d.Male_2005,
						+d.Male_2000,
						+d.Male_1995,
						+d.Male_1990,
						+d.Female_1990,
						+d.Female_1995,
						+d.Female_2000,
						+d.Female_2005,
						+d.Female_2010,
						+d.Female_2015,
						+d.Female_2019,
					]),
					Female_1995: +d.Female_1995,
					Female_2000: +d.Female_2000,
					Female_2005: +d.Female_2005,
					Female_2010: +d.Female_2010,
					Female_2015: +d.Female_2015,
					Female_2019: +d.Female_2019,
					Male_1995: +d.Male_1995,
					Male_2000: +d.Male_2000,
					Male_2005: +d.Male_2005,
					Male_2010: +d.Male_2010,
					Male_2015: +d.Male_2015,
					Male_2019: +d.Male_2019,
				},
			];
		});
	}

	$: {
		datapoints_from_app = sort(datapoints_from_app, (d) => d.Destination);
	}
	//$: console.log(datapoints_from_app);
	$: {
		datapoints_from_app.forEach((d) => {
			if (temp != d.Destination) {
				i = i + 15;
				start_i = 1;
			}
			y = start_i * spacing;
			datapoints_from_app[z].years = [];

			datapoints_from_app[z].Female_1990 = array_generator(
				datapoints_from_app[z].Female_1990,
				y
			);
			start_i = start_i + datapoints_from_app[z].Female_1990.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "1990": y });

			datapoints_from_app[z].Male_1990 = array_generator(
				datapoints_from_app[z].Male_1990,
				y
			);
			start_i = start_i + datapoints_from_app[z].Male_1990.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "1990": y });

			datapoints_from_app[z].Female_1995 = array_generator(
				datapoints_from_app[z].Female_1995,
				y
			);
			start_i = start_i + datapoints_from_app[z].Female_1995.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "1995": y });

			datapoints_from_app[z].Male_1995 = array_generator(
				datapoints_from_app[z].Male_1995,
				y
			);
			start_i = start_i + datapoints_from_app[z].Male_1995.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "1995": y });

			datapoints_from_app[z].Female_2000 = array_generator(
				datapoints_from_app[z].Female_2000,
				y
			);
			start_i = start_i + datapoints_from_app[z].Female_2000.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2000": y });

			datapoints_from_app[z].Male_2000 = array_generator(
				datapoints_from_app[z].Male_2000,
				y
			);
			start_i = start_i + datapoints_from_app[z].Male_2000.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2000": y });

			datapoints_from_app[z].Female_2005 = array_generator(
				datapoints_from_app[z].Female_2005,
				y
			);
			start_i = start_i + datapoints_from_app[z].Female_2005.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2005": y });
			datapoints_from_app[z].Male_2005 = array_generator(
				datapoints_from_app[z].Male_2005,
				y
			);
			start_i = start_i + datapoints_from_app[z].Male_2005.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2005": y });

			datapoints_from_app[z].Female_2010 = array_generator(
				datapoints_from_app[z].Female_2010,
				y
			);
			start_i = start_i + datapoints_from_app[z].Female_2010.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2010": y });

			datapoints_from_app[z].Male_2010 = array_generator(
				datapoints_from_app[z].Male_2010,
				y
			);
			start_i = start_i + datapoints_from_app[z].Male_2010.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2010": y });

			datapoints_from_app[z].Female_2015 = array_generator(
				datapoints_from_app[z].Female_2015,
				y
			);
			start_i = start_i + datapoints_from_app[z].Female_2015.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2015": y });
			datapoints_from_app[z].Male_2015 = array_generator(
				datapoints_from_app[z].Male_2015,
				y
			);
			start_i = start_i + datapoints_from_app[z].Male_2015.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2015": y });
			datapoints_from_app[z].Female_2019 = array_generator(
				datapoints_from_app[z].Female_2019,
				y
			);
			start_i = start_i + datapoints_from_app[z].Female_2019.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2019": y });

			datapoints_from_app[z].Male_2019 = array_generator(
				datapoints_from_app[z].Male_2019,
				y
			);
			start_i = start_i + datapoints_from_app[z].Male_2019.length;
			y = start_i * spacing;
			datapoints_from_app[z].years.push({ "2019": y });
			datapoints_from_app[z].X = i;
			datapoints_from_app[z].Y = y;
			z++;
			
			temp = d.Destination;
		});
	}

	$: maximum = max(
		datapoints_from_app.map((d) => {
			return d.Y;
		})
	);

	$: console.log(datapoints_from_app);
</script>

<!-- svelte-ignore a11y-no-onchange -->
<!-- add maximum in height_i-->
<Dotting datapoints={datapoints_from_app} height_i={maximum} />
