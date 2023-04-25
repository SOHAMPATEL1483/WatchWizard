<script>
  import ls from "localstorage-slim";
  import { djangoapi } from "../../app/stores";
  import { Circle } from "svelte-loading-spinners";
  import { invalidateAll } from "$app/navigation";
  import { error } from "@sveltejs/kit";
  // 43200
  let username = "";
  let password = "";
  let isloading = false;
  let errors = { username: "", password: "", all: "" };

  let login = true;
  const toggle_login = () => {
    login = !login;
    (username = ""), (password = "");
  };
  const validatedata = (
    /** @type {string} */ username,
    /** @type {string} */ password
  ) => {
    errors = { username: "", password: "", all: "" };
    if (username === "") errors.username = "username can't be empty";
    if (password === "") errors.password = "password can't be empty";
    if (password.length < 8)
      errors.password = "password must have 8 characters";
  };
  const setuserinfo = async () => {
    let jwt = ls.get("jwt");
    let res = await fetch(`${$djangoapi}/user/info/`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${jwt}`,
      },
    });
    let data = await res.json();
    ls.set("id", data.id, { ttl: 43200 });
    ls.set("username", data.username, { ttl: 43200 });
    invalidateAll();
  };

  const signin = async () => {
    isloading = true;
    validatedata(username, password);
    console.log(errors);
    if (errors.username != "" || errors.password != "" || errors.all != "") {
      isloading = false;
      return;
    }
    let res = await fetch(`${$djangoapi}/api/token/`, {
      method: "POST",
      body: JSON.stringify({ username: username, password: password }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    let token = await res.json();
    if (res.ok) {
      console.log(token);
      ls.set("jwt", token.access, { ttl: 43200 });
      await setuserinfo();
      // @ts-ignore
      window.location = "/home";
    } else {
      errors.all = token.detail;
      ls.clear();
    }
    (username = ""), (password = "");
    isloading = false;
    login = true;
    console.log(errors);
  };

  const signup = async () => {
    isloading = true;
    validatedata(username, password);
    if (errors.username != "" || errors.password != "" || errors.all != "") {
      isloading = false;
      return;
    }
    let res = await fetch(`${$djangoapi}/user/create/`, {
      method: "POST",
      body: JSON.stringify({ username: username, password: password }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    let token = await res.json();
    console.log(token);
    console.log(res.status);
    if (token.hasOwnProperty("id")) {
      console.log("succeess");
      //   console.log(token);
    } else {
      errors.all = token.username[0];
    }
    await signin();
    isloading = false;
    (username = ""), (password = "");
    console.log(errors);
  };
</script>

{#if login}
  <div class="h-full font-poppins">
    <div class="w-fit md:w-96 mx-auto mt-36">
      <div
        class="w-96 bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-[#27354c] dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold text-gray-900 md:text-2xl dark:text-white">
            Sign in to your account
          </h1>
          <div class="space-y-4 md:space-y-6">
            <div>
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Username</label>
              <input
                bind:value={username}
                type="text"
                name="email"
                id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="xyz123"
                required />
              {#if errors.username != ""}
                <p class="mt-1 text-sm font-medium text-red-500">
                  {errors.username}
                </p>
              {/if}
            </div>
            <div>
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Password</label>
              <input
                bind:value={password}
                type="password"
                name="password"
                id="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required />
              {#if errors.password != ""}
                <p class="mt-1 text-sm font-medium text-red-500">
                  {errors.password}
                </p>
              {/if}
            </div>
            {#if errors.all != ""}
              <p class="mt-1 text-sm font-medium text-red-500">
                {errors.all}
              </p>
            {/if}
            <button
              on:click={signin}
              class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
              {#if isloading}
                <div class="flex justify-center">
                  <Circle color="#f1f5f9" size="30" />
                </div>
              {:else}
                Sign In{/if}
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Don't have an account yet? <button
                on:click={toggle_login}
                class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                >Sign up</button>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
{:else}
  <div class="h-full font-poppins">
    <div class="w-96 mx-auto mt-36">
      <div
        class="w-96 bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-[#27354c] dark:border-gray-700">
        <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
          <h1
            class="text-xl font-bold text-gray-900 md:text-2xl dark:text-white">
            Create a new account
          </h1>
          <div class="space-y-4 md:space-y-6">
            <div>
              <label
                for="email"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Username</label>
              <input
                bind:value={username}
                type="text"
                name="email"
                id="email"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                placeholder="xyz123"
                required />
              {#if errors.username != ""}
                <p class="mt-1 text-sm font-medium text-red-500">
                  {errors.username}
                </p>
              {/if}
            </div>
            <div>
              <label
                for="password"
                class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                >Password</label>
              <input
                bind:value={password}
                type="password"
                name="password"
                id="password"
                placeholder="••••••••"
                class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                required />
              {#if errors.password != ""}
                <p class="mt-1 text-sm font-medium text-red-500">
                  {errors.password}
                </p>
              {/if}
            </div>
            {#if errors.all != ""}
              <p class="mt-1 text-sm font-medium text-red-500">
                {errors.all}
              </p>
            {/if}
            <button
              on:click={signup}
              class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
              {#if isloading}
                <div class="flex justify-center">
                  <Circle color="#f1f5f9" size="30" />
                </div>
              {:else}
                Sign up
              {/if}
            </button>
            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
              Already have an account? <button
                on:click={toggle_login}
                class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                >Sign in</button>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
{/if}
