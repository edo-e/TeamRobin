<script>
	import Papa from "papaparse";
	import Dotting from "./components/Dotting.svelte";
	import { max, sort } from "d3-array";
	import { scaleLinear, scaleLog } from "d3-scale";


	export var filename = ["Total_continent.csv"];
	export var target = [];

	let raw_data = [];
	let z = 0;
	let i = 50;
	let j = 50;
	let option_sort = ["Continent"];
	let datapoints_from_app = [];

	$: {
		datapoints_from_app = [];
		raw_data = [];
		Papa.parse(filename[0], {
			header: true,
			download: true,
			complete: function (results) {
				raw_data = results.data;
			},
		});
	}
	$: {
		raw_data.forEach((d) => {
			datapoints_from_app = [
				...datapoints_from_app,
				{
					Destination: d.Destination,
					X: +d.X,
					Y: +d.Y,
					Year: +d.Year,
					Origin: d.Origin,
					Region: d.Region,
					Continent: d.Continent,
					Female: +d.Female,
					Male: +d.Male,
				},
			];
		});
	}
	const radius = function (d) {
        if ((scale_r_dest(d) > 0) & (filename == "Total_destination.csv")) {
            return scale_r_dest(d);
        } else if (
            (scale_r_cont(d) > 0) &
            (filename == "Total_continent.csv")
        ) {
            return scale_r_cont(d);
        } else if (
            (scale_r_ori(d) > 0) &
            (filename== "Total_origin.csv")
        ) {
            return scale_r_ori(d);
        }  
        else return 1;
    };

	let origin_max= 35974445;
	let destination_max = 128209596;
	let continent_max =  216307703;
	let pad_circles =50;

    $: scale_r_ori = scaleLog().base(100).domain([5, 35974445]).range([5, 50]);
    $: scale_r_dest = scaleLog().base(100).domain([5, 128209596]).range([5, 50]);
    $: scale_r_cont = scaleLinear().domain([0, 216307703]).range([5, 250]);

	$: {
		datapoints_from_app = sort(
			datapoints_from_app,
			(d) => d[option_sort[0]]
		);
	}

	$: {
		if (
			filename == "Total_origin.csv"
		) {
			if ((z) => datapoints_from_app.length) {
				z = 0;
				j = radius(origin_max) + pad_circles;
				i = radius(origin_max) + pad_circles;
			}
			datapoints_from_app.forEach((d) => {
				if (z > 0) {
					if (i > 1250) {
						j =
							j + radius(origin_max) + pad_circles;
						i = radius(origin_max) + pad_circles;
					} else {
						i = i + radius(origin_max)+pad_circles;
					}
				}
				datapoints_from_app[z].X = i;
				datapoints_from_app[z].Y = j;
				z++;
			});
		}else if(filename == "Total_continent.csv"){
			if ((z) => datapoints_from_app.length) {
				z = 0;
				j = radius(continent_max) ;
				i = radius(continent_max) ;
			}
			datapoints_from_app.forEach((d) => {
				if (z > 0) {
					if (i > 800) {
						j = j + radius(continent_max) + 5*pad_circles;
						i = radius(continent_max) + pad_circles;
					} else {
						i = i + radius(continent_max) + 5*pad_circles;
					}
				}
				datapoints_from_app[z].X = i;
				datapoints_from_app[z].Y = j;
				z++;
			});
		}else if(filename == "Total_destination.csv" )		 {
			if ((z) => datapoints_from_app.length) {
				z = 0;
				j = radius(destination_max) + pad_circles;
				i = radius(destination_max) + pad_circles;
			}
			datapoints_from_app.forEach((d) => {
				if (z > 0) {
					if (i > 1250) {
						j =
							j + radius(destination_max) + pad_circles;
						i = radius(destination_max) + pad_circles;
					} else {
						i = i + radius(destination_max) +pad_circles;
					}
				}
				datapoints_from_app[z].X = i;
				datapoints_from_app[z].Y = j;
				z++;
			});
		}
	}

	
	$: {
		if (filename == "Total_origin.csv") {
			target[0] = "Origin";
		} else if (filename == "Total_continent.csv") {
			target[0] = "Continent";
		} else if (filename == "Total_destination.csv") {
			target[0] = "Destination";
		}
	}
	$: console.log(datapoints_from_app);

</script>

<!-- svelte-ignore a11y-no-onchange -->
<select multiple bind:value={option_sort} on:change={() => (z = 0)}>
	<option value="Destination"> Destination </option>
	<option value="Female"> Female </option>
	<option value="Male"> Male </option>
	<option value="Continent"> Continent </option>
	<option value="Region"> Region </option>
</select>

<select multiple bind:value={filename} on:change={() => (z = 0)}>
	<option value="Total_destination.csv"> By destination </option>
	<option value="Total_origin.csv"> By origin </option>
	<option value="Total_continent.csv"> By continent </option>
</select>

<Dotting datapoints={datapoints_from_app} target_dotting={target} filename_dotting ={filename} />
