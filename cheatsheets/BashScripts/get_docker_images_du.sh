#!/bin/bash

get_docker_images_du() {
    total_size=0
    while read -r id created; do
        if [[ ${created} == *weeks* || ${created} == *months* || ${created} == *years* ]]; then
            image_size=$(docker image inspect --format='{{.Size}}' $id)
            echo -n "Image ${id}: "
            echo "${image_size}" | awk '{print $1/1024/1024 " MB "}'

            total_size="$((total_size + image_size))"
        fi
    done < <(docker images --format "{{.ID}} {{.CreatedSince}}")

    echo -n "Total: "
    echo "${total_size}" | awk '{print $1/1024/1024/1024 " GB "}'
}

get_docker_images_du
