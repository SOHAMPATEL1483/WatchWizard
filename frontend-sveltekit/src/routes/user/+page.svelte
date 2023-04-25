<script>
  // @ts-nocheck

  import ls from "localstorage-slim";
  import { djangoapi } from "../../app/stores";
  import { onMount } from "svelte";

  let movies = [];
  const loadmovie = async () => {
    const headers = { Authorization: `Bearer ${ls.get("jwt")}` };
    let res = await fetch(`${$djangoapi}/user/getuser/`, {
      headers,
    });
    movies = await res.json();
    console.log(movies[0]);
  };

  onMount(() => {
    loadmovie();
  });
</script>

<div class="flex w-full flex-shrink-0 flex-col">
  <div class="mx-auto my-20 flex justify-center align-middle">
    <img
      class="h-40 rounded-full"
      src={`https://ui-avatars.com/api/?name=${ls.get(
        "username"
      )}&background=random`}
      alt="" />

    <h1
      class="text-slate-300 font-bold text-2xl font-poppins my-auto mx-10 text-center">
      {ls.get("username")}
    </h1>
  </div>

  <div class="px-5">
    {#each movies as movie}
      <a
        href={"/movie/" + movie.Imdb_id}
        class="flex my-5 mx-auto font-poppins items-center bg-white border rounded-lg max-w-2xl shadow hover:bg-gray-100 border-gray-700 dark:bg-gray-700">
        <img
          class="object-cover rounded-l-lg h-32"
          src={"https://image.tmdb.org/t/p/w200" + movie.Poste_path}
          alt="" />
        <div
          class="flex justify-between w-full p-4 ml-4 divide-x-2 divide-slate-600">
          <h5
            class="text-xl self-center font-bold tracking-wide text-slate-100">
            {movie.Title}
          </h5>
          <h5 class="text-slate-100 p-6 text-xl font-bold self-center">
            {movie.Rating}
          </h5>
        </div>
      </a>
    {/each}
  </div>
</div>
