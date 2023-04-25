<script>
  // @ts-nocheck

  import Crewcard from "$lib/crewcard.svelte";
  import { onMount } from "svelte";
  import StarRatting from "@ernane/svelte-star-rating";
  import { djangoapi } from "../../../app/stores.js";
  import ls from "localstorage-slim";

  export let data;

  //   let movieinfo = {
  //     backdrop: "https://image.tmdb.org/t/p/original",
  //     poster: "https://image.tmdb.org/t/p/w300",
  //     title: "",
  //     year: "",
  //     tagline: "",
  //     overview: "",
  //   };
  //   let cast = [];
  //   let director = { name: "", profile_path: "" };
  let config = {
    readOnly: false,
    countStars: 10,
    range: { min: 0, max: 10, step: 1 },
    score: 0,
    showScore: true,
    starConfig: {
      size: 30,
      fillColor: "#F9ED4F",
      strokeColor: "#BB8511",
      unfilledColor: "#71717a",
      strokeUnfilledColor: "#00000",
    },
  };

  //   const loadmovie = async () => {
  //     let res = await fetch(
  //       `https://api.themoviedb.org/3/movie/${data.slug}?api_key=843811a4e70cd56397b52a070f1ddf61`
  //     );
  //     let info = await res.json();
  //     if (info) {
  //       movieinfo.poster += info["poster_path"];
  //       movieinfo.backdrop += info["backdrop_path"];
  //       movieinfo.title = info["original_title"];
  //       movieinfo.overview = info["overview"];
  //       movieinfo.tagline = info["tagline"];
  //       movieinfo.year = info["release_date"].slice(0, 4);
  //     }
  //   };

  //   const loadcast = async () => {
  //     let res = await fetch(
  //       `https://api.themoviedb.org/3/movie/${data.slug}/credits?api_key=843811a4e70cd56397b52a070f1ddf61`
  //     );
  //     let info = await res.json();
  //     for (let i = 0; i < info["crew"].length; i++) {
  //       if (info["crew"][i]["job"] === "Director") {
  //         director = info["crew"][i];
  //       }
  //     }
  //     cast = info["cast"].slice(0, 5);
  //   };

  const loadrating = async () => {
    let headers = {};
    if (ls.get("jwt") != null)
      headers = { Authorization: `Bearer ${ls.get("jwt")}` };
    let res = await fetch(`${$djangoapi}/user/getmovie/?movieId=${data.slug}`, {
      headers,
    });
    let ratings = await res.json();
    if (ratings.Rating != null) {
      config.score = ratings.Rating;
      config.readOnly = true;
    }
  };

  onMount(async () => {
    loadrating();
    if (window.screen.width <= 768) {
      config.starConfig.size = 20;
    }
  });

  const changeSliderInput = async () => {
    let headers = {};
    if (ls.get("jwt") != null)
      headers = { Authorization: `Bearer ${ls.get("jwt")}` };
    let res = await fetch(
      `${$djangoapi}/user/training/?movieId=${data.slug}&rating=${config.score}`,
      {
        headers,
      }
    );
    console.log(res.status);
    config.readOnly = true;
  };
</script>

<div class="relative h-auto">
  <!-- content -->
  <div
    class="flex flex-col md:flex-row py-10 px-5 md:h-[38rem] md:px-28 align-middle">
    <div class="self-center flex-shrink-0">
      <img src={data.movieinfo.poster} alt="" class="rounded-xl" />
    </div>
    <div class="text-white md:p-10 self-center font-poppins w-auto">
      <p class="text-4xl my-5 font-extrabold">
        {data.movieinfo.title}
        <span class="text-slate-300">({data.movieinfo.year})</span>
      </p>
      <p class="italic text-slate-300">{data.movieinfo.tagline}</p>
      <div class="star-rating my-6 flex">
        {#if ls.get("jwt")}
          <div class="">
            <StarRatting bind:config on:change={changeSliderInput} />
          </div>
        {:else}
          <p class="text-red-200">Please Login to rate this movie</p>
        {/if}
      </div>
      <p class="my-3 text-xl font-semibold">Overview</p>
      <p class="">{data.movieinfo.overview}</p>
    </div>
  </div>
  <!-- image -->
  <!-- bg-[url('https://image.tmdb.org/t/p/w500/pbEkjhdfP7yuDcMB78YEZwgD4IN.jpg')] -->
  <div
    class="absolute top-0 -z-10 w-full h-[38rem] bg-no-repeat bg-cover invisible md:visible"
    style="background-position-y: 50%; background-image: linear-gradient(rgba(30, 41, 59, 0.7),rgba(30, 41, 59, 0.7)), url({data
      .movieinfo.backdrop})" />
</div>

<div
  class="flex flex-col md:flex-row py-10 md:divide-x-2 divide-slate-600 justify-center font-poppins">
  <!-- director -->
  <div class="pr-3">
    <p class="text-slate-300 m-5 text-xl">Director</p>
    <div class="flex justify-center">
      <Crewcard
        link={"https://image.tmdb.org/t/p/w300/" +
          data.director["profile_path"]}
        name={data.director["name"]} />
    </div>
  </div>
  <!-- crew -->
  <div class="pl-3">
    <p class="text-slate-300 m-5 text-xl">Cast</p>
    <div class="flex flex-wrap justify-center md:justify-start">
      {#each data.cast as person}
        <Crewcard
          link={"https://image.tmdb.org/t/p/w300/" + person["profile_path"]}
          name={person["name"]} />
      {/each}
    </div>
  </div>
</div>
