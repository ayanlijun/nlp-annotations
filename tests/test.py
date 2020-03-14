from nlp_annotations import (
    markdown_links2entity_list,
    entity_list2markdown_links
)


def test() -> None:
    tests = [
        {
            "markdown_links": "The weather is [sunny](weather) and the sky is [blue](color)",
            "entity_list": ('The weather is sunny and the sky is blue', {'entities': [(15, 20, 'weather'), (36, 40, 'color')]})
        }
    ]
    for t in tests:
        assert markdown_links2entity_list(t["markdown_links"]) == t["entity_list"]
        assert entity_list2markdown_links(t["entity_list"][0], t["entity_list"][1]["entities"])


if __name__ == "__main__":
    test()
