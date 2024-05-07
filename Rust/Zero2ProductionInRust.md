rustc --version
cargo --version

cargo new zero2prod - intialize new project
    ```
    zero2prod/
        cargo.toml
        .gitignore
        .git
        src/
            main.rs
    ```

- create new empty repo in github
    ```
    git add .
    git commit -am "Project Skeleton"
    git remote add origin git@github.com:GHNickname/zero2prod.git
    git push -u origin main
    ```

`Zero To Production will focus on the challenges of writing Cloud-native applications in a team of
four or five engineers with different levels of experience and proficiency`
- To achieve high-availability while running in the fault-prone environments
- To allow us to continuously release new versions with zero downtime
- To handl edynamic workloads(e.g. request volumes)


