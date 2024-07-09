#!/bin/bash

# Pedir al usuario que ingrese el nombre a buscar
echo "Ingrese el nombre a buscar en los commits:"
read nombre

# Buscar commits que coincidan con el nombre ingresado por el usuario
commits=$(git log --pretty=format:"%h %an %ar - %s" --grep="$nombre")

# Mostrar cada commit y sus cambios
echo "$commits" | while IFS= read -r commit; do
    commit_hash=$(echo "$commit" | awk '{print $1}')
    echo "$commit"

    # Obtener lista de archivos modificados en el commit
    files=$(git diff-tree --no-commit-id --name-only -r "$commit_hash")

    # Iterar sobre cada archivo y mostrar solo las líneas añadidas
    echo "$files" | while IFS= read -r file; do
        echo "Archivo: $file"
        # Utilizamos git diff para obtener solo las líneas añadidas del commit,
        # excluyendo las líneas de encabezado "++ b/"
        git diff --unified=0 "$commit_hash^" "$commit_hash" "$file" | grep '^\+[^\+]' | sed 's/^\+//'
        echo
    done

    echo
done
