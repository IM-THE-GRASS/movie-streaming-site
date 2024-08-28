import reflex as rx


class GlobalKeyWatcher(rx.Fragment):
    # List of keys to trigger on
    keys: rx.Var[list[str]] = []

    # The event handler that will be called
    bind: rx.EventHandler[lambda ev: [ev.key]]

    def _get_imports(self) -> rx.utils.imports.ImportDict:
        return rx.utils.imports.merge_imports(
            super()._get_imports(),
            {
                "react": {
                    rx.utils.imports.ImportVar(
                        tag="useEffect"
                    )
                }
            },
        )

    def _get_hooks(self) -> str | None:
        return """
            useEffect(() => {
                const handle_key = (_ev) => {
                    if (%s.includes(_ev.key))
                        %s
                }
                document.addEventListener("keydown", handle_key, false);
                return () => {
                    document.removeEventListener("keydown", handle_key, false);
                }
            })
            """ % (
            self.keys,
            rx.utils.format.format_event_chain(
                self.event_triggers["bind"]
            ),
        )

    def render(self):
        return ""  # No visual element, hooks only
Keybind = GlobalKeyWatcher.create